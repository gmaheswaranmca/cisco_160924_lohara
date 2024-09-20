import multiprocessing

def square(x, queue):
    queue.put(x * x)
if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=square, args=(4, queue))
    process.start()
    process.join()
    result = queue.get()
    print(result)