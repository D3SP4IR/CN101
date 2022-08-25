A = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]

B = [ [1, 3, 5],
      [7, 9, 2],
      [8, 4, 6] ]

for i in range(3):
    for j in range(3):
        A[i][j] += B[i][j]

for i in range(3):
    print(A[i])