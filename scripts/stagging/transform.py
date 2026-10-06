"""
==================================================================
Transform Functions
==================================================================
Scripts purpose: this script is to transform data that have been 
extract from CSV

this include data cleaning, data conversion, handling null value,
and key generation

Run this file by using 
silver_data = transform(bronze_data)

===================================================================
"""

import pandas as pd
from datetime import datetime

def transform(df):
    print("Transformation Starting.....")
    # Clean gender column
    print("Transformation of gender column")
    try:
        df["gender"] = (
            df["gender"].str.lower()
            .map({"male": "Male", "m": "Male", "female": "Female", "f": "Female"})
        )
        df["gender"] = df["gender"].fillna("Unknown")
    except Exception as e:
        print("Error cleaning gender column:", e)

    # Clean follow_up_required column
    print("Transformation of follow_up_required column")
    try:
        df["follow_up_required"] = df["follow_up_required"].astype(str).str.strip().str.lower()
        df["follow_up_required"] = df["follow_up_required"].replace({
            "1": "Yes", "yes": "Yes", "y": "Yes",
            "0": "No", "no": "No", "n": "No"
        })
    except Exception as e:
        print("Error cleaning follow_up_required column:", e)

    # Clean patient_name
    print("Transformation of patient_name column")
    try:
        df["patient_name"] = df["patient_name"].str.strip()

        df["patient_name"] =( df["patient_name"].str.replace(
        r"^(Dr|Miss|Mr|Mrs|Ms)\s+",
        "",
        regex=True,
        case=False).str.replace(
        r"\s+(DVM|MD|DDS|Jr|Sr|PhD)$",
        "",
        regex=True,
        case=False
    )
    .str.strip()
)
   
    except Exception as e:
        print("Error cleaning patient_name column:", e)

    # Clean doctor name
    print("Transformation of doctor column")
    try:
        df["doctor"] = df["doctor"].str.strip()
    except Exception as e:
        print("Error cleaning doctor column:", e)

    # Clean appointment_date
    print("Transformation of appointment_date column")
    try:
        df['appointment_date']=pd.to_datetime(df['appointment_date'],format='mixed',errors='coerce')
        df["appointment_date"] = df["appointment_date"].dt.strftime("%Y-%m-%d")
    except Exception as e:
        print("Error cleaning appointment_date column:", e)

    # Clean booking_date
    print("Transformation of booking_date column")
    try:
        df['booking_date']=pd.to_datetime(df['booking_date'],format='mixed',errors='coerce')
        df["booking_date"] = df["booking_date"].dt.strftime("%Y-%m-%d")
    except Exception as e:
        print("Error cleaning booking_date column:", e)

    # Clean billing_amount
    print("Transformation of billing_amount column")
    try:
        df["billing_amount"] = (
            df["billing_amount"].astype(str).str.replace("$", "", regex=False)
        ).astype(float)
        df["billing_amount"] = df["billing_amount"].fillna(0)
    except Exception as e:
        print("Error cleaning billing_amount column:", e)

    # Drop patient_id
    print("Dropping patient_id column")
    try:
        df = df.drop(columns=["patient_id"])
    except Exception as e:
        print("Error dropping patient_id column:", e)
      
   #generate patient_id, doctor_id and department_id
    df["patient_id"]=df.groupby(["patient_name", "age"], sort=False, dropna=False).ngroup() + 1000

    df["doctor_id"] = "d" + (df.groupby("doctor", sort=False, dropna=False).ngroup() + 1).astype(str)

    df["department_id"] = df.groupby("department", sort=False, dropna=False).ngroup() + 1

    df["dwh_create_date"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Transformation Finish")
    return df
