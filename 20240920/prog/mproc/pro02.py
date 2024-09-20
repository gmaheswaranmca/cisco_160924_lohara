import multiprocessing

lock = multiprocessing.Lock()
counter = multiprocessing.Value('i', 0)

def increment():
    global counter
    with lock:
        counter.value += 1

if __name__ == '__main__':
    processes = [multiprocessing.Process(target=increment) for _ in range(100)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(counter.value)