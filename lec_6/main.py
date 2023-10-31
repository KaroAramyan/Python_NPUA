import random

def generate_random_matrix(rows, cols):
 
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, col_index):
   
    column_sum = 0
    for row in matrix:
        if 0 <= col_index < len(row):
            column_sum += row[col_index]
    return column_sum

def get_row_average(matrix, row_index):

    if 0 <= row_index < len(matrix):
        row = matrix[row_index]
        if len(row) > 0:
            return sum(row) / len(row)
    return 0.0 


rows = 4
cols = 3
matrix = generate_random_matrix(rows, cols)
print("Generated Matrix:")
for row in matrix:
    print(row)

col_index = 1
column_sum = get_column_sum(matrix, col_index)
print(f"Sum of column {col_index}: {column_sum}")

row_index = 2
row_average = get_row_average(matrix, row_index)
print(f"Average of row {row_index}: {row_average}")
