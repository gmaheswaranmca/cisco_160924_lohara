from flask import Flask, jsonify, request  
from patient_db import Patient, patientTablesCreate, createPatient, readAllPatients     ###
from patient_db import searchByDisease, updatePatient, deletePatient, readPatientById         ###
patientTablesCreate()                                                  ###
app = Flask(__name__)

class e(Exception):
    print("ID NOT present in patients records")
@app.route('/patients',methods=['POST'])
def patients_create():
    body = request.get_json()
    new_patient = Patient(name=body['name'], age=body['age'],disease=body['disease'])
    id = createPatient(new_patient)
    patient = readPatientById(id)
    patient_dict = {'id':patient.id, 'name':patient.name, 'age':patient.age,'disease':patient.disease}
    return jsonify(patient_dict)

@app.route('/patients/<id>',methods=['GET'])
def patients_read_by_id(id):
    body = request.get_json()
    old_record = readPatientById(id)
    if not old_record:
        return jsonify({'message': 'Record is not found!'})
    patient = readPatientById(id)
    patient_dict = {'id':patient.id, 'name':patient.name, 'age':patient.age,'disease':patient.disease}
    return jsonify(patient_dict)
      

@app.route('/patients',methods=['GET'])
def patients_read_all():
    patients = readAllPatients()
    patients_dict = []
    for patient in patients:
        patients_dict.append({'id':patient.id, 'name':patient.name, 'age':patient.age,'disease':patient.disease})
    return jsonify(patients_dict)

@app.route('/patients/<id>',methods=['PUT'])
def patients_update(id):
    body = request.get_json()
    old_record = readPatientById(id)
    if not old_record:
        return jsonify({'message': 'Record is not found!'})
    old_record.name = body['name']
    old_record.age = body['age']
    old_record.disease=body['disease']
    updatePatient(old_record)
    patient = readPatientById(id)
    patient_dict = {'id':patient.id, 'name':patient.name, 'age':patient.age,'disease':patient.disease}
    return jsonify(patient_dict)

@app.route('/patients/<id>',methods=['DELETE'])
def patients_delete(id):
    old_record = readPatientById(id)
    if not old_record:
        return jsonify({'message': 'Record is not found', 'is_error': 1})
    deletePatient(id)
    return jsonify({'message': 'Record is successfully deleted', 'is_error': 0})

@app.route('/patients_search/<disease>',methods=['POST'])
def patients_search(disease):
    patient = searchByDisease(disease)
    patient_dict = {'id':patient.id, 'name':patient.name, 'age':patient.age,'disease':patient.disease}
    return jsonify(patient_dict)

app.run(debug=True)