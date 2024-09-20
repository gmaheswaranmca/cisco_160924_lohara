import threading

condition = threading.Condition()
chocolate_ready = False

prods = []
cons = []
batches = []
def producer():
    global chocolate_ready

    for I in range(1,15+1):
        with condition:
            prods.append(I)
            if I % 5 == 0:   
                batches.append(1)
                chocolate_ready = True
                condition.notify()

def consumer():
    while True:
        with condition:
            while not chocolate_ready:
                condition.wait()
            #print("Data is ready")
            cons.extend(prods) 
            prods.clear()
        if len(cons) >= 15:
            break

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()
print(cons, batches)
