'''
Main pipeline for OCR Data Extraction ETL

Flow:
1. Extract data from scanned documents
2. Clean and standardize the data
3. Validate extracted information
4. Export final result to Excel
'''

from src.extraction.pdf_extractor import extract_tables_from_pdf
from src.transform.cleaning import clean_table
from src.transform.normalization import normalize_column_names
from src.transform.validation import validate_minimum_columns, validate_table_not_empty
from src.utils.diagnostics import print_extraction_summary
from src.export.excel_exporter import export_tables_to_excel

def main() -> None:
    '''
    Run the OCR data extraction ETL pipeline.
    '''

    print("Starting OCR Data Extraction ETL Pipeline...")

    # Define path
    input_file = "ocr-data-extraction-etl/data/input/scanned_document.pdf"
    output_file = "ocr-data-extraction-etl/data/output/extracted_data.xlsx"
    total_pages = 10 

    try:
        
        print(f'Input file: {input_file}')
        print(f'Output file: {output_file}')

        # 1. Extraction
        # TODO:  call OCR extraction function
        extracted_tables, diagnostics = extract_tables_from_pdf(
            pdf_path = input_file,
            total_pages = total_pages,
        )

        print_extraction_summary(diagnostics)

        # 2. Transformation
        # TODO: call cleaning and standardization functions
        transformed_tables = []

        for sheet_name, raw_df in extracted_tables:
            cleaned_df = clean_table(raw_df)
            normalized_df = normalize_column_names(cleaned_df)

            transformed_tables.append((sheet_name, normalized_df))

        # 3. Validation
        # TODO: call automatic validation functions
        validation_report = []
        valid_tables = []

        for sheet_name, transformed_df in transformed_tables:
            not_empty_validation = validate_table_not_empty(transformed_df)

            minimum_columns_validation = validate_minimum_columns(
                transformed_df,
                min_columns=2,
            )

            is_valid = (
                not_empty_validation['is_valid'] and minimum_columns_validation['is_valid']
            )

            validation_report.append(
                {
                    'sheet_name': sheet_name,
                    'is_valid': is_valid,
                    'rows_found': not_empty_validation["rows_found"],
                    'columns_found': minimum_columns_validation["columns_found"],
                    'minimum_columns': minimum_columns_validation["minimum_columns"],
                    'not_empty': not_empty_validation["is_valid"],
                    'has_minimum_columns': minimum_columns_validation["is_valid"],
                }
            )

            if is_valid:
                valid_tables.append((sheet_name, transformed_df))

        # 4. Exportation
        # TODO: export result to Excel
        # export_to_excel(transformed_tables, diagnostic, output_file)

        print('Pipeline finished.')

    except FileNotFoundError as error:
        print(f"File not found: {error}")
    
    except PermissionError as error:
        print(f"Permission error: {error}")

    except ValueError as error:
        print(f"Value error: {error}")

    except RuntimeError as error:
        print(f"Runtime error: {error}")
    
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

    if __name__ == "__main__":
        main()