from db import VehicleTablesCreate, createVehicle, readAllVehicles, Vehicle

VehicleTablesCreate()

id = createVehicle(Vehicle(number='TN08K2004',type='TATA',price_per_hour=400))
print(f'{id} is inserted')
id = createVehicle(Vehicle(number='AP07KA2012',type='HONDA',price_per_hour=600))
print(f'{id} is inserted')

cabs = readAllVehicles()
print(cabs)
