# fib_iter.py

class FibonacciIterator:
    def __init__(self, stop=10):
        self.stop = stop
        self.start = 0
        self.cur = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.start += 1
            term = self.cur
            self.cur, self.next = self.next, (self.cur + self.next)
            return term
        else:
            raise StopIteration
            
            
for term in FibonacciIterator(5):
    print(term, end = ' ')
    
print()
fi = FibonacciIterator(3)
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
#print(fi.__next__())

def fibb_ser(stop=10):
    cur, next = 0, 1
    for I in range(stop):
        term = cur
        yield term
        cur, next = next, cur + next

for term in fibb_ser(5):
    print(term, end = ' ')




