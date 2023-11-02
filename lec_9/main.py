import random
class Matrix:
    def __init__(self, rows, cols):
      
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
      
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __add__(self, other):
    
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
      
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
     
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

# Example usage:
matrix1 = Matrix(2, 3)
matrix2 = Matrix(3, 2)

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

# Addition
result_addition = matrix1 + matrix2
print("\nAddition Result:")
print(result_addition)

# Subtraction
result_subtraction = matrix1 - matrix2
print("\nSubtraction Result:")
print(result_subtraction)

# Multiplication
result_multiplication = matrix1 * matrix2
print("\nMultiplication Result:")
print(result_multiplication)
