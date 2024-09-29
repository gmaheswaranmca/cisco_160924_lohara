from flask import Flask, jsonify, request
from db import Airplane, airplaneTablesCreate, createAirplane, readAllAirplanes, readAirplaneById, updateAirplane, deleteAirplane

airplaneTablesCreate()
app = Flask(__name__)

@app.route('/airplanes', methods=['POST'])
def airplanes_create():
    body = request.get_json()
    new_airplane = Airplane(model=body['model'], capacity=body['capacity'], status=body['status'])
    id = createAirplane(new_airplane)
    airplane = readAirplaneById(id)
    return jsonify({'id': airplane.id, 'model': airplane.model, 'capacity': airplane.capacity, 'status': airplane.status})

@app.route('/airplanes/<id>', methods=['GET'])
def airplanes_read_by_id(id):
    airplane = readAirplaneById(id)
    if airplane:
        return jsonify({'id': airplane.id, 'model': airplane.model, 'capacity': airplane.capacity, 'status': airplane.status})
    return jsonify({'message': 'Airplane not found'}), 404

@app.route('/airplanes', methods=['GET'])
def airplanes_read_all():
    airplanes = readAllAirplanes()
    return jsonify([{'id': a.id, 'model': a.model, 'capacity': a.capacity, 'status': a.status} for a in airplanes])

@app.route('/airplanes/<id>', methods=['PUT'])
def airplanes_update(id):
    body = request.get_json()
    airplane = readAirplaneById(id)
    if not airplane:
        return jsonify({'message': 'Airplane not found'}), 404
    airplane.model = body['model']
    airplane.capacity = body['capacity']
    airplane.status = body['status']
    updateAirplane(airplane)
    return jsonify({'id': airplane.id, 'model': airplane.model, 'capacity': airplane.capacity, 'status': airplane.status})

@app.route('/airplanes/<id>', methods=['DELETE'])
def airplanes_delete(id):
    airplane = readAirplaneById(id)
    if not airplane:
        return jsonify({'message': 'Airplane not found'}), 404
    deleteAirplane(id)
    return jsonify({'message': 'Airplane successfully deleted'})

app.run(debug=True)

