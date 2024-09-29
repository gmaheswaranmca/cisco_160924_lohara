from patient_db import patientTablesCreate, createPatient, readAllPatients, Patient

patientTablesCreate()

id = createPatient(Patient(name='Bhavz',age=22,disease='MU'))
print(f'{id} is inserted successfully')
id = createPatient(Patient(name='Charu',age=23,disease='DU'))
print(f'{id} is inserted successfully')

patients = readAllPatients()
print(patients)
