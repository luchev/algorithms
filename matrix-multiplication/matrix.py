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

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return self
        
        out = matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                out.data[i][j] = self.data[i][j] - other.data[i][j]
        return out

    def __str__(self):
        output = "-----\n"
        for i in range(self.rows):
            output += str(self.data[i]) + "\n"
        return output + "-----"

    def compareDimensions(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def canMultiply(self, other):
        return self.cols == other.rows

    def subMatrix(self, startRow, startCol, endRow, endCol):
        out = matrix(endRow - startRow + 1, endCol - startCol + 1)
        for i in range(startRow, endRow + 1):
            for j in range(startCol, endCol + 1):
                out.set(i - startRow, j - startCol, self.get(i, j))
        return out

    def clear(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = 0
    
    def fillToSquare(self):
        "Make the matrix dimensions 2^n x 2^n filling the new rows/cols with zeros"
        size = 1
        while size < self.rows and size < self.cols:
            size <<= 1
        
        for i in range(0, self.rows):
            for _ in range(size - self.cols):
                self.data[i].append(0)

        for i in range(size - self.rows):
            row = []
            for _ in range(size):
                row.append(0)
            self.data.append(row)

        self.rows = size
        self.cols = size
    
    def removeEmptyRows(self):
        for row in range(self.rows - 1, 0, -1):
            for col in range(self.cols):
                if self.data[row][col] != 0:
                    return

            del self.data[-1]
            self.rows -= 1

    def removeEmptyCols(self):
        for col in range(self.cols - 1, 0, -1):
            for row in range(self.rows):
                if self.data[row][col] != 0:
                    return
            
            for row in range(self.rows):
                del self.data[row][-1]
            self.cols -= 1

    def removeEmptyCells(self):
        self.removeEmptyRows()
        self.removeEmptyCols()
            