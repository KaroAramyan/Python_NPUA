import random

class Matrix:
    def __init__(self, n, m):
    
        self.rows = n
        self.cols = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
       
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
      
        total = sum(sum(row) for row in self.matrix)
        return total / (self.rows * self.cols)

    def calculate_row_sum(self, row_index):
       
        if 0 <= row_index < self.rows:
            return sum(self.matrix[row_index])
        return 0

    def calculate_column_average(self, col_index):
        
        if 0 <= col_index < self.cols:
            col_values = [row[col_index] for row in self.matrix]
            return sum(col_values) / self.rows
        return 0.0

    def print_submatrix(self, col1, col2, row1, row2):
      
        if 0 <= row1 <= row2 < self.rows and 0 <= col1 <= col2 < self.cols:
            for i in range(row1, row2 + 1):
                print(self.matrix[i][col1:col2 + 1])

# Example usage:
n = 4
m = 3
matrix = Matrix(n, m)
print("Generated Matrix:")
matrix.print_matrix()

mean = matrix.calculate_mean()
print(f"Mean of the matrix: {mean}")

row_index = 2
row_sum = matrix.calculate_row_sum(row_index)
print(f"Sum of row {row_index}: {row_sum}")

col_index = 1
col_average = matrix.calculate_column_average(col_index)
print(f"Average of column {col_index}: {col_average}")

col1, col2, row1, row2 = 1, 2, 1, 3
print(f"Submatrix [{row1}:{row2}, {col1}:{col2}]:")
matrix.print_submatrix(col1, col2, row1, row2)
