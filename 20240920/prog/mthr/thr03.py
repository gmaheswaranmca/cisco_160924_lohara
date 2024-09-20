import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)


""" 
import threading
from collections import defaultdict
from datetime import datetime


lock = threading.Lock()
counter = 0
states = defaultdict(list)
def increment():
    global counter
    thread_id = threading.get_ident()
    with lock:
        for _ in range(50):
            counter += 1
            states[thread_id].append(datetime.now().strftime("%H:%M:%S.%f"))
        

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)

print(repr(states))
 """