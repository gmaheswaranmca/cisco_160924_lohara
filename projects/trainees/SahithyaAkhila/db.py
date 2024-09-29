import sqlite3

def connect():
    con = sqlite3.connect('cabs_db.db')  # Renamed to match the cabs context
    return con

def vehicleTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS vehicles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_type VARCHAR(255) NOT NULL,
        vehicle_number VARCHAR(50) NOT NULL,
        price_per_hour REAL NOT NULL
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Vehicle:
    def __init__(self, id=None, vehicle_type='', vehicle_number='', price_per_hour=0.0):
        self.id = id
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number
        self.price_per_hour = price_per_hour
    
    def __str__(self):
        return f'[{self.id}, {self.vehicle_type}, {self.vehicle_number}, {self.price_per_hour}]'
    
    def __repr__(self):
        return self.__str__()

def createVehicle(vehicle):
    sql = """INSERT INTO vehicles(vehicle_type, vehicle_number, price_per_hour)
    VALUES(?, ?, ?)"""
    params = (vehicle.vehicle_type, vehicle.vehicle_number, vehicle.price_per_hour)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    id = cur.lastrowid
    con.commit()
    con.close()
    return id

def readAllVehicles():
    sql = """SELECT id, vehicle_type, vehicle_number, price_per_hour FROM vehicles"""
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql)
    result = response.fetchall()
    con.close()

    vehicles = []
    for row in result:
        vehicles.append(Vehicle(id=row[0], vehicle_type=row[1], vehicle_number=row[2], price_per_hour=row[3]))
    return vehicles

def searchVehicle(vehicle_type, vehicle_number):
    vehicle_type = vehicle_type.strip()
    vehicle_number = vehicle_number.strip()
    sql = """SELECT id, vehicle_type, vehicle_number, price_per_hour FROM vehicles
        WHERE (? == '' OR vehicle_type = ?) AND 
              (? == '' OR vehicle_number LIKE ('%' || ? || '%'))"""
    params = (vehicle_type, vehicle_type, vehicle_number, vehicle_number)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql, params)
    result = response.fetchall()
    con.close()

    vehicles = []
    for row in result:
        vehicles.append(Vehicle(id=row[0], vehicle_type=row[1], vehicle_number=row[2], price_per_hour=row[3]))
    return vehicles

def updateVehicle(vehicle):
    sql = """UPDATE vehicles
    SET vehicle_type = ?, vehicle_number = ?, price_per_hour = ?
    WHERE id = ?"""
    params = (vehicle.vehicle_type, vehicle.vehicle_number, vehicle.price_per_hour, vehicle.id)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()

def deleteVehicle(id):
    sql = """DELETE FROM vehicles
    WHERE id = ?"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()

def readVehicleById(id):
    sql = """SELECT id, vehicle_type, vehicle_number, price_per_hour FROM vehicles
    WHERE id = ?"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql, params)
    result = response.fetchone()
    con.close()

    if result:
        vehicle = Vehicle(id=result[0], vehicle_type=result[1], vehicle_number=result[2], price_per_hour=result[3])
    else:
        vehicle = None
    return vehicle