"""
==================================================================
ETL Scripts
==================================================================
Scripts purpose: this script is to perform complete ETL procedure
and load it to postgreSQL

===================================================================
"""
from python_script.extract import extract_csv
from python_script.transform import transform
from python_script.load import load_to_sql
import pandas as pd

bronze_data = extract_csv(file_path="Dataset/clinic_appointments.csv")

silver_data = transform(bronze_data)

load_to_sql(silver_data,table_name="clinic_appointments", schema="silver")
