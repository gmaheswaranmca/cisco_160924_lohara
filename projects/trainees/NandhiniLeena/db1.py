import sqlite3

def connect():
    con = sqlite3.connect('airticket_db.db')
    return con 
def AirplaneTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS Airplane(
        id integer primary key AUTOINCREMENT,
        flight_Number varchar(50) not null,
        seats_Available varchar(50) not null,
        ticket_Price varchar(50) not null
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Airplane:
    def __init__(self, id=None,flight_Number='',seats_Available='',ticket_Price=''):
        self.id = id 
        self.flight_Number=flight_Number
        self.seats_Available=seats_Available
        self.ticket_Price=ticket_Price

    def __str__(self):
        return f'[{self.id},{self.flight_Number},{self.seats_Available},{self.ticket_Price}]'
    def __repr__(self):
        return self.__str__()

def createTicket(ticket):
    sql = """INSERT INTO Airplane(flight_Number,seats_Available,ticket_Price)
    VALUES(?,?,?)"""
    params = (ticket.flight_Number, ticket.seats_Available,ticket.ticket_Price)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    id = cur.lastrowid  
    con.commit()
    con.close()
    return id           

def readAllPassengers():
    sql = """SELECT id,flight_Number,seats_Available,ticket_Price FROM Airplane"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    passengers = [] # [Note(id=row[0],title=row[1],notes=row[2]) for row in result]
    for row in result:
        passengers.append(Airplane(id=row[0],flight_Number=row[1],
                seats_Available=row[2],ticket_Price=row[3]))
    return passengers

def search(flight_Number):
    flight_Number = flight_Number.strip()
    sql = """SELECT * FROM passengers
        WHERE ( ? == '' OR flight_Number=?))"""
    params = (flight_Number,flight_Number)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    passengers = []
    for row in result:
        passengers.append(Airplane(id=row[0],flight_Number=row[1],
                seats_Available=row[2],ticket_Price=row[3]))
    return passengers

def update(ticket):
    sql = """UPDATE passengers
    set flight_Number=?,seats_Available=?,ticket_Price=?
    WHERE (id=?)"""
    params = (ticket.flight_Number,ticket.seats_Available,ticket.ticket_Price,
              ticket.id,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
def delete(id):
    sql = """DELETE from passengers
    WHERE (id=?)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
    
def readById(id):
    sql = """SELECT flight_Number,seats_Available,ticket_Price FROM passengers
    WHERE (id=?)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone() #row=[id,title,...]
    con.close()

    if result != None:
        ticket = Airplane(id=result[0],flight_Number=result[1],
                    seats_Available=result[2],ticket_Price=result[3])
    else:
        ticket = None 
    return ticket
