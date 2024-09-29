from flask import Flask, jsonify, request
from db import Vehicle, vehicleTablesCreate, createVehicle, readAllVehicles
from db import searchVehicle, updateVehicle, deleteVehicle, readVehicleById

# Initialize the database tables
vehicleTablesCreate()

# Create the Flask app
app = Flask(__name__)

# POST: Create a new vehicle
@app.route('/vehicles', methods=['POST'])
def vehicles_create():
    body = request.get_json()
    if not body:
        return jsonify({'message': 'Request body is missing'}), 400
    try:
        new_vehicle = Vehicle(
            vehicle_type=body['vehicle_type'], 
            vehicle_number=body['vehicle_number'], 
            price_per_hour=body['price_per_hour']
        )
        id = createVehicle(new_vehicle)
        vehicle = readVehicleById(id)
        vehicle_dict = {
            'id': vehicle.id, 
            'vehicle_type': vehicle.vehicle_type, 
            'vehicle_number': vehicle.vehicle_number, 
            'price_per_hour': vehicle.price_per_hour
        }
        return jsonify(vehicle_dict), 201
    except Exception as e:
        return jsonify({'message': 'Error creating vehicle', 'error': str(e)}), 500

# GET: Retrieve a vehicle by ID
@app.route('/vehicles/<int:id>', methods=['GET'])
def vehicles_read_by_id(id):
    vehicle = readVehicleById(id)
    if vehicle:
        vehicle_dict = {
            'id': vehicle.id, 
            'vehicle_type': vehicle.vehicle_type, 
            'vehicle_number': vehicle.vehicle_number, 
            'price_per_hour': vehicle.price_per_hour
        }
        return jsonify(vehicle_dict)
    else:
        return jsonify({'message': 'Vehicle not found'}), 404

# GET: Retrieve all vehicles
@app.route('/vehicles', methods=['GET'])
def vehicles_read_all():
    vehicles = readAllVehicles()
    vehicles_dict = [{
        'id': vehicle.id, 
        'vehicle_type': vehicle.vehicle_type, 
        'vehicle_number': vehicle.vehicle_number, 
        'price_per_hour': vehicle.price_per_hour
    } for vehicle in vehicles]
    return jsonify(vehicles_dict)

# PUT: Update a vehicle by ID
@app.route('/vehicles/<int:id>', methods=['PUT'])
def vehicles_update(id):
    body = request.get_json()
    if not body:
        return jsonify({'message': 'Request body is missing'}), 400
    vehicle = readVehicleById(id)
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404

    try:
        vehicle.vehicle_type = body['vehicle_type']
        vehicle.vehicle_number = body['vehicle_number']
        vehicle.price_per_hour = body['price_per_hour']
        updateVehicle(vehicle)
        vehicle_dict = {
            'id': vehicle.id, 
            'vehicle_type': vehicle.vehicle_type, 
            'vehicle_number': vehicle.vehicle_number, 
            'price_per_hour': vehicle.price_per_hour
        }
        return jsonify(vehicle_dict)
    except Exception as e:
        return jsonify({'message': 'Error updating vehicle', 'error': str(e)}), 500

# DELETE: Delete a vehicle by ID
@app.route('/vehicles/<int:id>', methods=['DELETE'])
def vehicles_delete(id):
    vehicle = readVehicleById(id)
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404
    try:
        deleteVehicle(id)
        return jsonify({'message': 'Vehicle successfully deleted'})
    except Exception as e:
        return jsonify({'message': 'Error deleting vehicle', 'error': str(e)}), 500

# POST: Search for vehicles
@app.route('/vehicles_search', methods=['POST'])
def vehicles_search():
    body = request.get_json()
    if not body:
        return jsonify({'message': 'Request body is missing'}), 400
    vehicles = searchVehicle(
        vehicle_type=body.get('vehicle_type', ''), 
        vehicle_number=body.get('vehicle_number', '')
    )
    vehicles_dict = [{
        'id': vehicle.id, 
        'vehicle_type': vehicle.vehicle_type, 
        'vehicle_number': vehicle.vehicle_number, 
        'price_per_hour': vehicle.price_per_hour
    } for vehicle in vehicles]
    return jsonify(vehicles_dict)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
