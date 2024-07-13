def matrix_transpose(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  transpose = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
  return transpose


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Original matrix:")
for row in matrix:
  print(row)
  
print("\nTranspose of the matrix:")
transpose = matrix_transpose(matrix)
for row in transpose:
  print(row)