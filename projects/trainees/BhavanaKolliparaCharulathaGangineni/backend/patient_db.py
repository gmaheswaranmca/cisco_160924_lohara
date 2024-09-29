import sqlite3

def connect():
    con = sqlite3.connect('patients_db.db')
    return con 
def patientTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS patients(
        id integer primary key AUTOINCREMENT,
        name varchar(255) not null,
        age int not null,
        disease varchar(255) not null
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Patient:
    def __init__(self, id=None,
        name='',
        age='',
        disease=''):
        self.id = id 
        self.name = name 
        self.age = age
        self.disease = disease
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Age: {self.age}, Diagnosed with: {self.disease}'
    def __repr__(self):
        return self.__str__()

def createPatient(patient):
    sql = """INSERT INTO patients(name, age, disease)
    VALUES(?,?,?)"""
    params = (patient.name, patient.age,patient.disease)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    id = cur.lastrowid  
    con.commit()
    con.close()
    return id           

def readAllPatients():
    sql = """SELECT id,name,age,disease FROM patients"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() 
    con.close()

    patients = []
    for row in result:
        patients.append(Patient(id=row[0],name=row[1],
                age=row[2],disease=row[3]))
    return patients 

def searchByDisease(disease):
    sql = """SELECT id,name,age,disease FROM patients
    WHERE (disease=?)"""
    params = (disease,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone()
    con.close()

    if result != None:
        patient = Patient(id=result[0],name=result[1],
                    age=result[2],disease=result[3])
    else:
        patient = None 
    return patient 

def updatePatient(patient):
    sql = """UPDATE patients
    set name=?,age=?,disease=?
    WHERE (id=?)"""
    params = (patient.name, patient.age,patient.disease,patient.id,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
def deletePatient(id):
    sql = """DELETE from patients
    WHERE (id=?)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
    
def readPatientById(id):
    sql = """SELECT id,name,age,disease FROM patients
    WHERE (id=?)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone()
    con.close()

    if result != None:
        patient = Patient(id=result[0],name=result[1],
                    age=result[2],disease=result[3])
    else:
        patient = None 
    return patient
