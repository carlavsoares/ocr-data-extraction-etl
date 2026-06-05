'''
PDF table extraction module.

This module extracts tables from scanned PDF files using OCR (Optical Character Recognition) techniques. 
It utilizes libraries such as PyPDF2 for PDF processing and Tesseract OCR for text extraction.
The extracted tables are then structured into a format suitable for further analysis or storage.    
'''

import gc
from pathlib import Path

import pandas as pd
from img2table.document import PDF
from img2table.ocr import PaddleOCR


# extract tables from a scanned PDF file
def extract_tables_from_pdf(
        pdf_path: str,
        total_pages: int,
        language: str = 'pt',
        min_confidence: int = 50
        
):
# return type hint for a tuple containing a list of tuples (sheet name and DataFrame) 
# and a list of dictionaries (diagnostics)

    '''
    Extract tables from a scanned PDF file.
    
    Args:
        pdf_path: Path to the input PDF file.
        total_pages: Total number of pages to process.
        language: OCR language. 
        min_confidence: Minimum OCR results confidence score.

    Returns:
    A tuple containing:
        - extracted_tables: list of tuples with sheet name and DataFrame.
        - diagnostics: list of dictionaries with extraction metadata.
    '''
    
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    if total_pages is None or total_pages <= 0:
        raise ValueError("total_pages must be a positive integer.")

    extracted_tables: list[tuple[str, pd.DataFrame]] = []  # List to store extracted tables as tuples of (sheet_name, DataFrame)
    diagnostics: list[dict] = []  # List to store diagnostics information for each page

    try:
        ocr_engine = PaddleOCR(lang=language)

    except Exception as error:
        raise RuntimeError(f"Failed to initialize OCR engine: {error}") from error

    # loop through each page of the PDF and extract tables
    for page_index in range(total_pages):
        print(f'Processing page {page_index + 1}/{total_pages}...')

        pdf = None # Initialize PDF variable to None to ensure it is defined in the scope of the try block
        tables = None # Initialize tables variable to None to ensure it is defined in the scope of the try block

        try:
            pdf = PDF(
                src = pdf_path,
                pages = [page_index],
                detect_rotation = True,
                pdf_text_extraction = False
            )

            tables = pdf.extract_tables(
                ocr = ocr_engine, 
                implicit_rows = True,
                implicit_columns = True,
                borderless_tables = True,
                min_confidence=min_confidence,
                max_workers=1
            )   
            
            total_tables = sum(len(table_list) for table_list in tables.values())
            
            diagnostics.append(
                {
                'page': page_index + 1,
                'status': 'success',
                'tables_found': total_tables,
                'error': None
                }
            )  
            
            for _, table_list in tables.items():
                for table_number, table in enumerate(table_list, start=1):
                    df = table.df  # Convert the table to a DataFrame       

                    if df is None or df.empty:
                        continue

                    sheet_name = f'Page_{page_index + 1}_Table_{table_number}'
                    extracted_tables.append((sheet_name, df))  # Append the sheet name and DataFrame as a tuple to the extracted_tables list    


        except Exception as error:
            print(f'Error processing page {page_index + 1}: {error}')

            diagnostics.append(
                {
                'page': page_index + 1,
                'status': 'error',
                'tables_found': 0,
                'error': str(error)
                }
            )
        finally:
            if pdf is not None:
                del pdf  # Explicitly delete the PDF object to free memory

            if tables is not None:
                del tables  # Explicitly delete the tables variable to free memory

            gc.collect()  # Clean up memory after processing each page    

    return extracted_tables, diagnostics