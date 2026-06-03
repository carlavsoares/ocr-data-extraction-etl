'''
Diagnostics utilities.
'''

def print_extraction_summary(diagnostics: list[dict]) -> None:
    '''
    Prints a summary of the extraction process.
    '''
    
    if not diagnostics:
        print('\nNo diagnostics available.')
        return
    
    print('\nExtraction sumary:')   

    for item in diagnostics:
        try:
            page_or_file = item.get("page", item.get("file", "unknown"))
            tables_found = item.get("tables_found", 0)
            status = item.get("status", "unknown")
            error = item.get("error")

            print(f'- Page/Fele {page_or_file}:')
            print(f'{tables_found} table(s) found | status: {status}')

            if error:
                print(f'    Error:{error}')
            
        except AttributeError:
            print( '- Invalid diagnostic item found.')
