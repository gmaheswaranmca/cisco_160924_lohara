""" import time
import threading
def print_numbers():
    thread_id = threading.get_ident()
    for i in range(5):
        print(f'@{thread_id}:{i}')
        time.sleep(1)
class MyThread(threading.Thread):
    def run(self):
        thread_id = threading.get_ident()
        for i in range(5):
            print(f'@{thread_id}:{i}')
            time.sleep(1)


thread1 = MyThread()
thread2 = MyThread()
thread1.start()  # Start the thread
thread2.start()  # Start the thread
thread1.join()   # Wait for the thread to finish
thread2.join()   # Wait for the thread to finish
print_numbers() """

import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(i)

thread = MyThread()
thread.start()
thread.join()
