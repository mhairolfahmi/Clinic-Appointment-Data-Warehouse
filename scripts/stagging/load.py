"""
==================================================================
Load Functions
==================================================================
Scripts purpose: this script is to load data that have been
transform to postgreSQL


Run this file by using 
load_to_sql(silver_data,table_name="clinic_appointments", 
schema="silver")

===================================================================
"""
import pandas as pd
from sqlalchemy import create_engine

def load_to_sql(df,table_name="clinic_appointments",schema="silver",
                db_url="postgresql+psycopg2://postgres:password@localhost:5432/clinic"):
    try:
        print('loading data into PostgreSQL....')
        engine=create_engine(db_url)

        df.to_sql(name=table_name,
                  con=engine,
                  schema=schema,
                  if_exists='replace',
                  index=False)
        print(f"Data successfully loaded")
    except Exception as e:
        print("Error loading data into PostgreSQL:", e)
