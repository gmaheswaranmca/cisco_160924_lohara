import threading

condition = threading.Condition()
data_ready = False

def producer():
    global data_ready
    with condition:
        data_ready = True
        condition.notify()

def consumer():
    with condition:
        while not data_ready:
            condition.wait()
        print("Data is ready")

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()