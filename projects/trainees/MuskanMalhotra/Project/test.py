from db import cabVehicleTableCreate, createCabVehicle, readAllCabVehicles, CabVehicle

cabVehicleTableCreate()

createCabVehicle(CabVehicle(vehicle_no='CAB123', category='Sedan', fare=25.0))
print(f'CAB123 is inserted')
createCabVehicle(CabVehicle(vehicle_no='CAB456', category='SUV', fare=40.0))
print(f'CAB456 is inserted')

cab_vehicles = readAllCabVehicles()
print(cab_vehicles)
