'''MULTIPLY MATRIX'''

import numpy as np

#Dimensi matrix
matrix_dimension = int(input())

#Mengisi matrix a
matrix_a_line_str = (input()).split()

matrix_a_line_int = []
for num in matrix_a_line_str:
    num = int(num)
    matrix_a_line_int.append(num)


matrix_a = np.array([matrix_a_line_int])

for line in range(1,matrix_dimension):
    matrix_a_line_str = (input()).split()
    
    matrix_a_line_int = []
    for num in matrix_a_line_str:
        num = int(num)
        matrix_a_line_int.append(num)
    
    matrix_a = np.vstack([matrix_a,matrix_a_line_int])

print(matrix_a)


#Mengisi matrix b
matrix_b_line_str = (input()).split()

matrix_b_line_int = []
for num in matrix_b_line_str:
    num = int(num)
    matrix_b_line_int.append(num)


matrix_b = np.array([matrix_b_line_int])

for line in range(1,matrix_dimension):
    matrix_b_line_str = (input()).split()
    
    matrix_b_line_int = []
    for num in matrix_b_line_str:
        num = int(num)
        matrix_b_line_int.append(num)
    
    matrix_b = np.vstack([matrix_b,matrix_b_line_int])

print(matrix_b)



#Mengalikan matrix a dan matrix b
matrix_multiplication = np.matmul(matrix_a,matrix_b)
print(matrix_multiplication)

matrix_multiplication = matrix_a@matrix_b
print(matrix_multiplication)

matrix_multiplication = np.dot(matrix_a,matrix_b)
print(matrix_multiplication)


def multiply_matrix(A,B):
  global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(matrix_dimension): 
        for col in range(matrix_dimension):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C
  else:
    return "Sorry, cannot multiply A and B."

matrix_multiplication = multiply_matrix(matrix_a,matrix_b)
print(matrix_multiplication)