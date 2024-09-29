import sqlite3

def connect():
    con = sqlite3.connect('vehicle_db.db')
    return con 
def VehicleTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS vehicles(
        id integer primary key AUTOINCREMENT,
        number integer not null,
        type varchar(2000) not null,
        price_per_hour integer not null)"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Vehicle:
    def __init__(self, id=None,
        number='',
        type='',
        price_per_hour=''):
        self.id = id 
        self.number = number
        self.type = type
        self.price_per_hour=price_per_hour
    def __str__(self):
        return f'[{self.id},{self.number},{self.type},{self.price_per_hour}]'
    def __repr__(self):
        return self.__str__()

def createVehicle(cab):
    sql = """INSERT INTO vehicles(number, type,price_per_hour)
    VALUES(?,?,?)"""
    params = (cab.number, cab.type,cab.price_per_hour)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    id = cur.lastrowid  
    con.commit()
    con.close()
    return id           

def readAllVehicles():
    sql = """SELECT id,number, type, price_per_hour FROM Vehicles"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() 
    con.close()

    cabs = []
    for row in result:
        cabs.append(Vehicle(id=row[0],number=row[1],
                type=row[2],price_per_hour=row[3]))
    return cabs 

def search(number, cabs_text):
    number = number.strip()
    cabs_text = cabs_text.strip()
    sql = """SELECT id,number,type,price_per_hour FROM cabs
        WHERE ( ? == '' OR number=?) AND 
              ( ? == '' OR type like ('%' || ? || '%'))"""
    params = (number,number, cabs_text,cabs_text)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    cabs = []
    for row in result:
        cabs.append(Vehicle(id=row[0],number=row[1],
                type=row[2],price_per_hour=row[3]))
    return cabs 

def updateVehicle(cab):
    sql = """UPDATE cabs
    set number=?,type=?,price_per_hour=?
    WHERE (id=?)"""
    params = (cab.number, cab.type,cab.price_per_hour,
              cab.id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
def deleteVehicle(id):
    sql = """DELETE from cabs
    WHERE (id=?)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
    
def readVehicleById(id):
    sql = """SELECT id,number, type,price_per_hour FROM cabs
    WHERE (id=?)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone() #row=[id,title,...]
    con.close()

    if result != None:
        cab = Vehicle(id=result[0],number=result[1],
                    type=result[2],price_per_hour=result[4])
    else:
        cab = None 
    return cab