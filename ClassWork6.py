# def matrix_sum(matrix1, matrix2):
#     if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix1[0]):
#         raise ValueError("Matrices must have the same dimensions to be summed.")
    
#     result_matrix = [[0 for column in row] for row in matrix1]

#     for m in range(len(matrix1)):
#         for n in range(len(matrix1[0])):
#             result_matrix[n][m] = matrix1[n][m] + matrix2[n][m]

#     return result_matrix 


# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# result_matrix = matrix_sum(matrix1, matrix2)
# print(result_matrix)



# def transpose_matrix(matrix):
#     transpose_matrix = [list(row) for row in zip(*matrix)]
#     return transpose_matrix

# original_matrix = [
#         [1, 2, 3],
#         [4, 5, 6], 
#         [7, 8, 9]
#     ]

# transpose_matrix = transpose_matrix(original_matrix)
# print(transpose_matrix)


# fruits = ["apple", "banana", "cherry"] 
# colors = ["red", "yellow", "green"] 
# for fruit, color in zip(fruits, colors): 
#     print(fruit, "is", color) 


# def multiply_matrix_by_scalar(matrix, scalar):
    
#     result_matrix = [[element * scalar for element in row] for row in matrix]
#     return result_matrix

# original_matrix = [[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
# scalar = 3

# result_matrix = multiply_matrix_by_scalar(original_matrix, scalar)
# print(result_matrix)



# def determinantOfMatrix(mat, n):
 
#     temp = [0]*n  # temporary array for storing row
#     total = 1
#     det = 1  # initialize result
 
#     # loop for traversing the diagonal elements
#     for i in range(0, n):
#         index = i  # initialize the index
 
#         # finding the index which has non zero value
#         while(index < n and mat[index][i] == 0):
#             index += 1
 
#         if(index == n):  # if there is non zero element
#             # the determinant of matrix as zero
#             continue
 
#         if(index != i):
#             # loop for swapping the diagonal element row and index row
#             for j in range(0, n):
#                 mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
 
#             # determinant sign changes when we shift rows
#             # go through determinant properties
#             det = det*int(pow(-1, index-i))
 
#         # storing the values of diagonal row elements
#         for j in range(0, n):
#             temp[j] = mat[i][j]
 
#         # traversing every row below the diagonal element
#         for j in range(i+1, n):
#             num1 = temp[i]     # value of diagonal element
#             num2 = mat[j][i]   # value of next row element
 
#             # traversing every column of row
#             # and multiplying to every row
#             for k in range(0, n):
#                 # multiplying to make the diagonal
#                 # element and next row element equal
 
#                 mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])
 
#             total = total * num1  # Det(kA)=kDet(A);
 
#     # multiplying the diagonal elements to get determinant
#     for i in range(0, n):
#         det = det*mat[i][i]
 
#     return int(det/total)  # Det(kA)/k=Det(A);
 
 
# # Drivers code
# if __name__ == "__main__":
#     # mat=[[6 1 1][4 -2 5][2 8 7]]
 
#     mat = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
#     N = len(mat)
     
#     # Function call
#     print("Determinant of the matrix is : ", determinantOfMatrix(mat, N))




import numpy as np 

array1 = np.random.random((5, 5))  
array2 = np.random.random((5, 5))

elementwise_product = np.multiply(array1, array2)

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)
print("\nElement-wise product:")
print(elementwise_product)