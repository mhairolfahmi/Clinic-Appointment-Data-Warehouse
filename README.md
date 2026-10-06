# Clinic Appointment Data Warehouse

## Projects Introduction

As the hospital’s business grows, MedicCare Clinic have attracts more patients and generates an increasing amount of data.

To manage the growing volume of data, the hospital has decided to build a data warehouse.

Hence, this project aims to design a data pipeline that extracts data from CSV files, transforms and cleans the data using Python, and loads the processed data into a PostgreSQL database for storage and future analysis.

## Dataset
the dataset used in this projects include column patient_id ,patient_name, age, gender,appointment_date, booking_date, doctor, department, billing_amount, follow_up_required.

## Data Quality
there are several issue with this dataset whixh are:
* gender = Null value, have inconsistent format (example Male, male, nan).
* follow_up_required = Have inconsistent format (ex: yes, y,1).
* appointment_date = Have inconsistent format.
* booking_date =  Have inconsistent format.
* billing_amount = Have inconsistent format (have $ symbol), Null value.
* patient_id = Corrupted column where same number is assigned to many customer.
* There is no doctor id and department id.

## Data Architecture

<img width="800" height="500" alt="data architecture" src="https://github.com/user-attachments/assets/5338167a-a4b8-448a-8237-f738f3fac905" />

## Data Flow
<img width="800" height="500" alt="Data Flow" src="https://github.com/user-attachments/assets/84cfb223-876c-423a-8b52-682c040059f4" />

## Data Modeling
<img width="800" height="500" alt="data modelling" src="https://github.com/user-attachments/assets/6db37f57-1147-4a4b-8822-02ac05a64f37" />

## Technology Used
* Python - pandas
* VS Code
* PostgreSQL


