'''
Data normalization functions.
'''

import re
import unicodedata

import pandas as pd

def normalize_text(text: object) -> str:
    '''
    Normalize text by removing accents, extras spaces, and removing special characters.
    '''
    if text is None:
        return ""   
    
    try:
        if pd.isna(text):
            return ""
    
    except TypeError:
        pass    

    text = str(text).strip().lower()

    text = unicodedata.normalize('NFKD', text)
    text = ''.join(
        char for char in text if not unicodedata.combining(char)
    )

    text = re.sub(r'[â-Z0-9]+', ' ', text)
    text = re.sub(r'_+','_', text)
    text = text.strip('_')

    return text

def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Normalize DataFrame column names.
    '''

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    df = df.copy()
    df.columns = [normalize_text(column) for column in df.columns]

    return df