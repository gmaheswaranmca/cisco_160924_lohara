from db1 import AirplaneTablesCreate, createTicket, readAllPassengers, Airplane

AirplaneTablesCreate()

id = createTicket(Airplane(flight_Number='1001',seats_Available='30',ticket_Price='5000'))
print(f'{id} is inserted')
id = createTicket(Airplane(flight_Number='1002',seats_Available='30',ticket_Price='5000'))
print(f'{id} is inserted')

notes = readAllPassengers()
print(notes)
