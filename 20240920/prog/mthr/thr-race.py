import time 
import threading
lock = threading.Lock()
total = 0
def print_numbers():
    global total 
    #id = threading.get_ident()
    for i in range(500000):
        #print(f'{i}@{id}')
        #time.sleep(0.025)
        with lock:
            total = total + 1

threads = []
for I in range(5):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()  # Start the thread
print(total)
