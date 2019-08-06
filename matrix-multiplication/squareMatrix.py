class squareMatrix:
    def __init__(self, size):
        self.size = size
        self.data = []
        for i in range(size):
            self.data.append([])
            for _ in range(size):
                self.data[i].append(0)
    
    def set(self, row, col, value):
        if row >= self.size or col >= self.size:
            return
        self.data[row][col] = value

    def get(self, row, col):
        if row >= self.size or col >= self.size:
            return
        return self.data[row][col]

    def getSize(self):
        return self.size
