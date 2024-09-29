from db import vehicleTablesCreate, createVehicle, readAllVehicles, Vehicle

vehicleTablesCreate()

id = createVehicle(Vehicle(vehicle_type='TATA NEXON', vehicle_number='ABC123', price_per_hour=20.0))
print(f'{id} is inserted')
id = createVehicle(Vehicle(vehicle_type='FERRARI', vehicle_number='XYZ789', price_per_hour=30.0))
print(f'{id} is inserted')

vehicles = readAllVehicles()
print(vehicles)