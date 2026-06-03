'''
Excel exporter module.
'''
from pathlib import Path

import pandas as pd

def export_tables_to_excel(
        tables: list[tuple[str, pd.DataFrame]],
        diagnostics: list[dict],
        validation_report: list[dict],
        output_path: str,
    ) -> None:
    '''
    Exports extracted tablesand diagnostics to an Excel file.

    Args:
        tables: List of tuples containing sheet names and DataFrames.
        diagnostics: A list of extraction diagnostics.
        validation_report: List of validation results.
        output_path: The path to the output Excel file.
    '''
    # Ensure the output directory exists
    output_file = Path(output_path)

    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            if tables:
                for sheet_name, df in tables:
                    if not isinstance(df, pd.DataFrame):
                        continue

                    safe_sheet_name = str(sheet_name)[:31]  # Excel sheet names must be <= 31 characters

                    df.to_excel(
                        writer, 
                        sheet_name=safe_sheet_name, 
                        index=False,
                    )

            else:
                pd.DataFrame({'Message': ['No tables extracted']}).to_excel(
                    writer, 
                    sheet_name='warming', 
                    index=False
                )
            
            pd.DataFrame(diagnostics).to_excel(
                writer, 
                sheet_name='diagnostics', 
                index=False,
            )
            pd.DataFrame(validation_report).to_excel(
                writer,
                sheet_name="validation",
                index=False,
            )

    except PermissionError:
       raise PermissionError(
           f'Could not write the Excel file'
           f'Check if the file is open in another program or you have write permissions: {output_path}'
       ) from error
    
    except FileNotFoundError:
        raise FileNotFoundError(
            f'Invalid output path: {output_path}'
        ) from error
    
    except Exception as error:
        raise RuntimeError(
            f'Failed to export tables to Excel: {error}'
        ) from error