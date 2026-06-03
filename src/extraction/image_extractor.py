'''
Image table extraction module.

This module extracts tables from scanned PDF files using OCR (Optical Character Recognition) techniques.
'''
from pathlib import Path

import pandas as pd
from img2table.document import Image
from img2table.ocr import PaddleOCR

def extract_tables_from_image(
        image_path: str,
        language: str = "pt",
        min_confidence: int = 50
) -> tuple[list[tuple[str, pd.DataFrame]], list[dict]]:
    
    '''
    Extract tables from a scanned image file.
    
    Args:
        image_path: Path to the input image file.
        language: OCR language.
        min_confidence: Minimum OCR results confidence score to consider a table valid.

    Returns:
        A tuple containing:
        - extracted_tables: list of tuples with sheet name and DataFrame of the extracted tables.
        - diagnostics: list of dictionaries with extraction metadata.   
    '''
    
    image_file = Path(image_path)

    if not image_file.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")

    extracted_tables: list[tuple[str, pd.DataFrame]] = []
    diagnostics: list[dict] = []

    try:
        ocr_engine = PaddleOCR(lang=language)
    
    except Exception as error:
        raise RuntimeError(f"Failed to initialize OCR engine: {error}") from error
  
    try:
        document = Image(
            src = str(image_file),
            detect_rotation = True,
        )

        tables = document.extract_tables(
            ocr = ocr_engine,
            implicit_rows = True,
            implicit_columns = True,
            borderless_tables = True,
            min_confidence = min_confidence,                              
        )

        diagnostics.append({
            'file': str(image_file),
            'status': 'success',    
            'tables_found': len(tables),
            'error': None,            
        })

        for table_number, table in enumerate(tables, start=1):
            df = table.df  # Convert the extracted table to a DataFrame

            if df is None or df.empty:
                continue  # Skip empty tables   

            sheet_name = f"{image_file.stem}_table_{table_number}"
            extracted_tables.append((sheet_name, df))

    except Exception as error:
        print(f'Error processing image file: {error}')

        diagnostics.append(
            {
            'file': str(image_file),
            'status': 'error',
            'tables_found': 0,
            'error': str(error),
            }
        )

    return extracted_tables, diagnostics