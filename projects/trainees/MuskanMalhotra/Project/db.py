import sqlite3

def connect():
    con = sqlite3.connect('cab_vehicles_db.db')
    return con 


def cabVehicleTableCreate():
    sql = """CREATE TABLE IF NOT EXISTS cab_vehicles(
        vehicle_no TEXT PRIMARY KEY,
        category TEXT NOT NULL,
        fare REAL NOT NULL
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Cab Vehicles table created and in sync.")


class CabVehicle:
    def __init__(self, vehicle_no, category, fare):
        self.vehicle_no = vehicle_no
        self.category = category
        self.fare = fare

    def __str__(self):
        return f'[vehicle_no={self.vehicle_no}, category={self.category}, fare={self.fare}]'

    def __repr__(self):
        return self.__str__()


def add_cab_vehicle(cab_vehicle):
    sql = """INSERT INTO cab_vehicles(vehicle_no, category, fare) VALUES (?, ?, ?)"""
    params = (cab_vehicle.vehicle_no, cab_vehicle.category, cab_vehicle.fare)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()
    print("Cab vehicle added successfully")


def read_all_cab_vehicles():
    sql = """SELECT vehicle_no, category, fare FROM cab_vehicles"""
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql)
    result = response.fetchall()
    con.close()

    cab_vehicles = []
    for row in result:
        cab_vehicles.append(CabVehicle(vehicle_no=row[0], category=row[1], fare=row[2]))
    return cab_vehicles


def read_cab_vehicle_by_no(vehicle_no):
    sql = """SELECT vehicle_no, category, fare FROM cab_vehicles WHERE vehicle_no = ?"""
    params = (vehicle_no,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql, params)
    result = response.fetchone()
    con.close()

    if result:
        return CabVehicle(vehicle_no=result[0], category=result[1], fare=result[2])
    else:
        return None


def update_cab_vehicle(cab_vehicle):
    sql = """UPDATE cab_vehicles SET category = ?, fare = ? WHERE vehicle_no = ?"""
    params = (cab_vehicle.category, cab_vehicle.fare, cab_vehicle.vehicle_no)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()
    print("Cab vehicle updated successfully")


def remove_cab_vehicle(vehicle_no):
    sql = """DELETE FROM cab_vehicles WHERE vehicle_no = ?"""
    params = (vehicle_no,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()
    print("Cab vehicle removed successfully")

if __name__ == "__main__":
    cabVehicleTableCreate() 
    
    while True:
        menu_option = input('Menu:\n1. Add Cab Vehicle\n2. Display All Cab Vehicles\n3. Find Cab Vehicle by Number\n4. Update Cab Vehicle\n5. Delete Cab Vehicle\n0. Exit\nEnter your choice: ')

        if menu_option == '1':
            vehicle_no = input('Enter cab vehicle number: ')
            category = input('Enter cab vehicle category: ')
            fare = float(input('Enter cab vehicle fare: '))
            cab_vehicle = CabVehicle(vehicle_no, category, fare)
            add_cab_vehicle(cab_vehicle)

        elif menu_option == '2':
            cab_vehicles = read_all_cab_vehicles()
            if cab_vehicles:
                for cab in cab_vehicles:
                    print(cab)
            else:
                print('No cab vehicles available.')

        elif menu_option == '3':
            vehicle_no = input('Enter cab vehicle number: ')
            cab_vehicle = read_cab_vehicle_by_no(vehicle_no)
            if cab_vehicle:
                print(cab_vehicle)
            else:
                print(f'Cab vehicle with number {vehicle_no} not found.')

        elif menu_option == '4':
            vehicle_no = input('Enter cab vehicle number to update: ')
            cab_vehicle = read_cab_vehicle_by_no(vehicle_no)
            if cab_vehicle:
                print(cab_vehicle)
                category = input(f'Enter new category (current: {cab_vehicle.category}): ') or cab_vehicle.category
                fare = float(input(f'Enter new fare (current: {cab_vehicle.fare}): '))
                cab_vehicle.category = category
                cab_vehicle.fare = fare
                update_cab_vehicle(cab_vehicle)
            else:
                print(f'Cab vehicle with number {vehicle_no} not found.')

        elif menu_option == '5':
            vehicle_no = input('Enter cab vehicle number to delete: ')
            remove_cab_vehicle(vehicle_no)

        elif menu_option == '0':
            break

        else:
            print('Invalid option, please try again.')
