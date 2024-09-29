from flask import Flask, jsonify, request
from db import Vehicle, VehicleTablesCreate, createVehicle, readAllVehicles   
from db import search, updateVehicle, deleteVehicle, readVehicleById        
VehicleTablesCreate()   
                                               
app = Flask(__name__)

@app.route('/cabs',methods=['POST'])
def cabs_create():
    body = request.get_json()
    new_cab = Vehicle(number=body['number'], type=body['type'],price_per_hour=body['price_per_hour'])
    id = createVehicle(new_cab)
    cab = readVehicleById(id)
    cab_dict = {'id':cab.id, 'number':cab.number, 'type':cab.type ,'price_per_hour':cab.price_per_hour}
    return jsonify(cab_dict)

@app.route('/cabs/<id>',methods=['GET'])
def cabs_read_by_id(id):
    cab = readVehicleById(id)
    cab_dict = {'id':cab.id, 'number':cab.number, 'type':cab.type ,'price_per_hour':cab.price_per_hour}
    return jsonify(cab_dict)

@app.route('/cabs',methods=['GET'])
def cabs_read_all():
    cabs = readAllVehicles()
    cabs_dict = []
    for cab in cabs:
        cabs_dict.append({'id':cab.id, 'number':cab.number, 'type':cab.type ,'price_per_hour':cab.price_per_hour})
    return jsonify(cabs_dict)

@app.route('/cabs/<id>',methods=['PUT'])
def cabs_update(id):
    body = request.get_json()
    old_note = readVehicleById(id)
    if not old_note:
        return jsonify({'message': 'Cab is not found'})
    old_note.number = body['number']
    old_note.type = body['type']
    old_note.price_per_hour = body['price_per_hour']
    updateVehicle(old_note)
    cab = readVehicleById(id)
    cab_dict = {'id':cab.id, 'number':cab.number, 'type':cab.type ,'price_per_hour':cab.price_per_hour}
    return jsonify(cab_dict)

@app.route('/cabs/<id>',methods=['DELETE'])
def cabs_delete(id):
    old_note = readVehicleById(id)
    if not old_note:
        return jsonify({'message': 'Cab is not found', 'is_error': 1})
    deleteVehicle(id)
    return jsonify({'message': 'Cab is successfully deleted', 'is_error': 0})

@app.route('/cabs_search',methods=['POST'])
def cabs_search():
    body = request.get_json()
    cabs = search(body.get('number',''), body.get('cabs_text',''))
    cabs_dict = []
    for cab in cabs:
        cabs_dict.append({'id':cab.id, 'number':cab.number, 'type':cab.type ,'price_per_hour':cab.price_per_hour})
    return jsonify(cabs_dict)

app.run(debug=True)