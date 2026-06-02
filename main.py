'''
Main pipeline for OCR Data Extraction ETL

Flow:
1. Extract data from scanned documents
2. Clean and standardize the data
3. Validate extracted information
4. Export final result to Excel
'''

def main():

    print("Starting OCR Data Extraction ETL Pipeline...")

    # 1. Define path
    input_file = "ocr-data-extraction-etl/data/input/scanned_document.pdf"
    output_file = "ocr-data-extraction-etl/data/output/extracted_data.xlsx"

    print(f'Input file: {input_file}')
    print(f'Output file: {output_file}')

    # 2. Extraction
    # TODO:  call OCR extraction function
    # extracted_tables, diagnostic = extract_pdf_tables(input_file)

    # 3. Transformation
    # TODO: call cleaning and standardization functions
    # transformed_tables = transform_tables(extracted_tables)

    # 4. Validation
    # TODO: call automatic validation functions
    # validation_report = validate_tables(transformed_tables)

    # 5. Exportation
    # TODO: export result to Excel
    # export_to_excel(transformed_tables, diagnostic, output_file)

    print('Pipeline finished.')

if __name__ == "__main__":
    main()


# git add main.py
# git commit -m "Initial commit of main pipeline structure" 