class fibonacci_sequence:
    def __init__(self, x):
        self.x = x
        self.a = 0
        self.b = 1
        self.seq = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.seq) < self.x:
            self.a, self.b = self.b, self.a + self.b
            self.seq.append(self.a)
            return int(self.seq[-1])
        else:
            raise StopIteration
