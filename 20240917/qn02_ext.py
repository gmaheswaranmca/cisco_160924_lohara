import json 
patients = [{'id':1,'name':'rahul'},{'id':2,'name':'modiji'}]
with open('qn02_patients.json','w') as patients_db:
    json.dump(patients, patients_db)
print('List of patients written json file db.')
with open('qn02_patients.json','r') as patients_db:
    patients2 = json.load(patients_db)
    print(f'Patients:{patients2}')