import multiprocessing
import time
import random


class Airplane:
    def __init__(self,id):
        self.airplane_id = id
        self.is_available = True

    def assign(self):
        self.is_available = False

    def release(self):
        self.is_available = True


class AirplaneManagementSystem:
    def __init__(self, num_airplanes):
        self.airplanes = multiprocessing.Manager().list([Airplane(i) for i in range(1, num_airplanes+1)])
        self.lock = multiprocessing.Lock()

    def find_available_Airplane(self):
        with self.lock:  # Critical section: Only one process can access the flights at a time
            for airplane in self.airplanes:
                if airplane.is_available:
                    return airplane
        return None

    def request_Airplane(self, user_id):
        print(f"User {user_id} is requesting a flight...")
        airplane = self.find_available_Airplane()
        if airplane:
            airplane.assign()
            print(f"Airplane {airplane.airplane_id} assigned to user {user_id}.")
            # Simulate the user holding the flight for a random duration
            time.sleep(random.randint(2, 5))
            airplane.release()
            print(f"Airplane {airplane.airplane_id} is now available after serving user {user_id}.")
        else:
            print(f"No flight available for user {user_id}. Please wait.")
            time.sleep(3)
            self.request_Airplane(user_id)  # Try again after some time


def simulate_user_requests(system, user_id):
    system.request_Airplane(user_id)


if __name__ == "__main__":
    num_airplanes = 3  # Let's assume there are 3 flights
    num_users = 6  # Let's assume there are 6 users requesting flights
    airplane_system = AirplaneManagementSystem(num_airplanes)

    processes = []
    
    # Create separate processes for each user request
    for i in range(1, num_users+1):
        process = multiprocessing.Process(target=simulate_user_requests, args=(airplane_system, i))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
