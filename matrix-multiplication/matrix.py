class matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []
        for i in range(rows):
            self.data.append([])
            for _ in range(cols):
                self.data[i].append(0)

    def set(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            return
        self.data[row][col] = value

    def get(self, row, col):
        if row >= self.rows or col >= self.cols:
            return
        return self.data[row][col]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return self
        
        out = matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                out.data[i][j] = self.data[i][j] + other.data[i][j]
        return out

    def __str__(self):
        return str(self.data)

    def compareDimensions(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def canMultiply(self, other):
        return self.cols == other.rows

    def subMatrix(self, startRow, startCol, endRow, endCol):
        out = matrix(endRow - startRow)