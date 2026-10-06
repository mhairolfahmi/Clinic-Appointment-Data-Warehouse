"""
==================================================================
Extract Functions
==================================================================
Scripts purpose: this script is to extract raw data from CSV file

Run this file by using 
data = extract_csv(file_path="Dataset/clinic_appointments.csv")

===================================================================
"""

import pandas as pd

def extract_csv(file_path):
    """
    Extract data from csv file

    """
    try:
        df=pd.read_csv(file_path)
        print(f"sucessfully extracted {len(df)} rows from {file_path}")
        return df
    

    except FileNotFoundError:
        print(f"Filenot found:{file_path}")
        return None

    except Exception as e:
        print(f"Error extracting csv:{e}")
        return None
