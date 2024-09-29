import threading
from time import sleep

class CabVehicle:
    def __init__(self, vehicle_no, category, fare):  
        self.vehicle_no = vehicle_no
        self.category = category
        self.fare = fare

    def __str__(self):  
        return f'[vehicle_no={self.vehicle_no}, category={self.category}, fare={self.fare}]'

cab_vehicles = []
lock = threading.Lock()  # To ensure thread safety

def add_cab_vehicle(vehicle_no, category, fare):
    cab_vehicle = CabVehicle(vehicle_no, category, fare)
    with lock:
        cab_vehicles.append(cab_vehicle)
        print(f'Cab vehicle {vehicle_no} added successfully')

def remove_cab_vehicle(vehicle_no):
    with lock:
        for cab_vehicle in cab_vehicles:
            if cab_vehicle.vehicle_no == vehicle_no:
                cab_vehicles.remove(cab_vehicle)
                print(f'Cab vehicle {vehicle_no} deleted successfully')
                return
        print(f'No such cab vehicle {vehicle_no}')

def display_cab_vehicles():
    with lock:
        if cab_vehicles:
            for cab_vehicle in cab_vehicles:
                print(cab_vehicle)
        else:
            print("No cab vehicles available.")

# Create multiple threads for adding, removing, and displaying vehicles
threads = []

# Adding vehicles in threads
threads.append(threading.Thread(target=add_cab_vehicle, args=("123", "Sedan", 25.0)))
threads.append(threading.Thread(target=add_cab_vehicle, args=("456", "SUV", 40.0)))
threads.append(threading.Thread(target=add_cab_vehicle, args=("789", "Hatchback", 20.0)))

# Removing a vehicle in thread
threads.append(threading.Thread(target=remove_cab_vehicle, args=("456",)))

# Displaying vehicles in a thread
threads.append(threading.Thread(target=display_cab_vehicles))

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished executing.")
