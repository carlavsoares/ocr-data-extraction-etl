'''
Validation functions for extracted tables.
'''

import pandas as pd

def validate_minimum_columns(
        df: pd.DataFrame, 
        min_columns: int = 2,
    ) -> dict:
    '''
    validate if the DataFrame has at least a minimum number of columns.
    '''

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    if min_columns <= 0:
        raise ValueError("min_columns must be greater than 0")
    
    is_valid = df.shape[1] >= min_columns

    return {
        "is_valid": is_valid,
        "columns_found": df.shape[1],
        "minimum_columns": min_columns,
    }

def validate_table_not_empty(df: pd.DataFrame) -> dict:
    '''
    Validate if the DataFrame is not empty.
    '''

    if df is None:
        return {
            "is_valid": False,
            "rows_found": 0,
            "columns_found": 0,
            "reason": "DataFrame is None"
        }
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    is_valid = not df.empty

    return {
        "is_valid": is_valid,
        "rows_found": df.shape[0],
        "columns_found": df.shape[1],
    }

