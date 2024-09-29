from db import airplaneTablesCreate, createAirplane, readAllAirplanes,readAirplaneById, Airplane

# Create the database tables
airplaneTablesCreate()

# Insert sample airplanes
id1 = createAirplane(Airplane(model='Boeing 747', capacity=416, status='Active'))
print(f'Airplane with ID {id1} created: Boeing 747, Capacity: 416, Status: Active')

id2 = createAirplane(Airplane(model='Airbus A380', capacity=555, status='Inactive'))
print(f'Airplane with ID {id2} created: Airbus A380, Capacity: 555, Status: Inactive')

id3 = createAirplane(Airplane(model='Cessna 172', capacity=4, status='Active'))
print(f'Airplane with ID {id3} created: Cessna 172, Capacity: 4, Status: Active')

# Read all airplanes to verify
airplanes = readAllAirplanes()
print("\nAll Airplanes in Database:")
for airplane in airplanes:
    print(f'ID: {airplane.id}, Model: {airplane.model}, Capacity: {airplane.capacity}, Status: {airplane.status}')

# Optionally, you can test reading a specific airplane by ID
print("\nTesting read by ID:")
test_id = 1  # Change this to any valid ID to test
airplane = readAirplaneById(test_id)
if airplane:
    print(f'Airplane with ID {test_id}: Model: {airplane.model}, Capacity: {airplane.capacity}, Status: {airplane.status}')
else:
    print(f'Airplane with ID {test_id} not found.')

# Note: You can also add tests for updating and deleting airplanes here.
