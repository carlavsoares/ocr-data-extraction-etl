'''
Data cleaning functions for extracted OCR tables.
'''

import pandas as pd

def validate_dataframe(df: pd.DataFrame) -> None:
    '''
    Validate if the input is a pandas DataFrame.
    '''
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Remove rows that are completely empty from the DataFrame.
    '''

    validate_dataframe(df)
    return df.dropna(how='all')

def remove_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Remove columns that are completely empty from the DataFrame.
    '''

    validate_dataframe(df)
    return df.dropna(axis=1, how='all')

def strip_text_values(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Remove leading and trailing whitespace from text cells.
    '''

    validate_dataframe(df)

    return df.map(
        lambda value: value.strip() if isinstance(value, str) else value
    )

def clean_table(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Apply basic cleaning steps to the DataFrame.
    '''

    validate_dataframe(df)

    df = remove_empty_rows(df)
    df = remove_empty_columns(df)
    df = strip_text_values(df)

    return df