import numpy as np

def vec_mat(vector, matrix):

    vector = np.array(vector)
    
 
    matrix = np.array(matrix)

    if vector.shape[0] != matrix.shape[1]:
        raise ValueError("Vector and matrix dimensions are not compatible for multiplication.")

    result = np.dot(vector, matrix)
    
    return result

def write_file(result, matvec):
    with open(matvec, 'w') as file:
        file.write(','.join(map(str, result)) + '\n')


vector = [2, 3]
matrix = [[1, 2], [3, 4]]

result = vec_mat(vector, matrix)

write_file(result, 'result.txt')
