class a:
    def __init__(self):
        self.start = self.current = 0
        self.end = 10
    def __iter__(self):
        if self.current >= self.end: raise StopIteration
        res = self.current
        self.current += 1
        return res

o = a()
print(o)
for value in o: print(value)
????