import sqlite3
import json

# Database connection
def connect():
    con = sqlite3.connect('airplanes_db.db')
    return con

# Create airplane table
def airplaneTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS airplanes(
        id integer primary key AUTOINCREMENT,
        model varchar(255) not null,
        capacity integer not null,
        status varchar(50) not null
    )"""
    con = connect()
    con.execute(sql)
    con.close()

# Airplane class
class Airplane:
    def __init__(self, id=None, model='', capacity=0, status=''):
        self.id = id
        self.model = model
        self.capacity = capacity
        self.status = status

# CRUD operations for airplanes
def createAirplane(airplane):
    sql = """INSERT INTO airplanes(model, capacity, status)
             VALUES(?,?,?)"""
    params = (airplane.model, airplane.capacity, airplane.status)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    id = cur.lastrowid
    con.commit()
    con.close()
    return id

def readAllAirplanes():
    sql = """SELECT id, model, capacity, status FROM airplanes"""
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql)
    result = response.fetchall()
    con.close()
    return [Airplane(id=row[0], model=row[1], capacity=row[2], status=row[3]) for row in result]

def readAirplaneById(id):
    sql = """SELECT id, model, capacity, status FROM airplanes WHERE id=?"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql, params)
    result = response.fetchone()
    con.close()
    if result:
        return Airplane(id=result[0], model=result[1], capacity=result[2], status=result[3])
    return None

def updateAirplane(airplane):
    sql = """UPDATE airplanes SET model=?, capacity=?, status=? WHERE id=?"""
    params = (airplane.model, airplane.capacity, airplane.status, airplane.id)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()

def deleteAirplane(id):
    sql = """DELETE FROM airplanes WHERE id=?"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()