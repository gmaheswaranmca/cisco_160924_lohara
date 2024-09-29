import threading
import time
import random

class Cab:
    def __init__(self, cab_id):
        self.cab_id = cab_id
        self.is_available = True

    def assign(self):
        self.is_available = False

    def release(self):
        self.is_available = True


class CabManagementSystem:
    def __init__(self, num_cabs):
        self.cabs = [Cab(i) for i in range(1, num_cabs+1)]
        self.lock = threading.Lock()

    def find_available_cab(self):
        with self.lock:  # Critical section: Only one thread can access the cabs at a time
            for cab in self.cabs:
                if cab.is_available:
                    return cab
        return None

    def request_cab(self, user_id):
        print(f"User {user_id} is requesting a cab...")
        cab = self.find_available_cab()
        if cab:
            cab.assign()
            print(f"Cab {cab.cab_id} assigned to user {user_id}.")
            # Simulate the user holding the cab for a random duration
            time.sleep(random.randint(2, 5))
            cab.release()
            print(f"Cab {cab.cab_id} is now available after serving user {user_id}.")
        else:
            print(f"No cabs available for user {user_id}. Please wait.")
            time.sleep(3)
            self.request_cab(user_id)  # Try again after some time


def simulate_user_requests(system, num_users):
    threads = []
    for i in range(1, num_users+1):
        thread = threading.Thread(target=system.request_cab, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    num_cabs = 3  # Let's assume there are 3 cabs
    num_users = 6  # Let's assume there are 6 users requesting cabs
    cab_system = CabManagementSystem(num_cabs)

    simulate_user_requests(cab_system, num_users)
