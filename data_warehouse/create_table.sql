"""
==================================================================
create table on sql before load data from python
==================================================================
Scripts purpose: this script is to create table with desired data
types

===================================================================
"""

DROP TABLE IF EXISTS silver.clinic_appointments;
CREATE TABLE silver.clinic_appointments (
patient_name VARCHAR(50),
age INTEGER,
gender VARCHAR(10),
appointment_date DATE,
booking_date DATE,
doctor VARCHAR(50),
department VARCHAR(50),
billing_amount INTEGER,
follow_up_required VARCHAR(10),
patient_id INTEGER,
doctor_id VARCHAR(10),
department_id INTEGER,
dwh_create_date TIMESTAMP
);

SELECT *
FROM silver.clinic_appointments;
