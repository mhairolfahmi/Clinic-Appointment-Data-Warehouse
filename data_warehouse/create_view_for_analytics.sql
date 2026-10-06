"""
==================================================
this scripts to create view to ready for analytics
==================================================

"""

-- CREATE VIEW OF DIM_PATIENTS
CREATE OR REPLACE VIEW gold.dim_patients AS
SELECT 
ROW_NUMBER()OVER(ORDER BY patient_id) as patient_key,
patient_id,
patient_name,
age,
gender
FROM (SELECT DISTINCT patient_id,patient_name,age,gender FROM silver.clinic_appointments)t;

-- CREATE DIM_DOCTOR VIEW

CREATE OR REPLACE VIEW gold.dim_doctors AS
SELECT 
ROW_NUMBER()OVER(ORDER BY doctor) as doctor_key,
doctor_id,
doctor AS doctor_name
FROM (SELECT DISTINCT doctor_id,doctor FROM silver.clinic_appointments)t;

--CREATE DIM_department

CREATE OR REPLACE VIEW gold.dim_departments AS
SELECT
ROW_NUMBER()OVER(ORDER BY department) as department_key,
department_id,
department
FROM (SELECT DISTINCT department_id,department FROM silver.clinic_appointments)t;

-- CREATE FACT_CLINIC_APPOINTMENT

CREATE OR REPLACE VIEW gold.facts_clinic_appointments AS
SELECT 
ca.appointment_date AS appointment_date,
ca.booking_date AS booking_date,
ROW_NUMBER()OVER(ORDER BY ca.booking_date) AS booking_id,
p.patient_key AS patient_key,
d.doctor_key AS doctor_key,
de.department_key AS department,
ca.billing_amount AS billing_amount,
ca.follow_up_required AS followed_up_required
FROM silver.clinic_appointments AS ca
INNER JOIN gold.dim_patients as p
ON ca.patient_id=p.patient_id
INNER JOIN gold.dim_doctors AS d
ON ca.doctor_id = d.doctor_id
INNER JOIN gold.dim_departments AS de
ON ca.department_id=de.department_id
ORDER BY appointment_date;
