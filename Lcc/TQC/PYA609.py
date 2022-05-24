m1 = [[0 for i in range(2)] for j in range(2)]
m2 = [[0 for i in range(2)] for j in range(2)]

print("Enter matrix 1:")
for i in range(2):
    for j in range(2):
        m1[i][j] = int(input("[{:d}, {:d}]: ".format(i+1,j+1)))

print("Enter matrix 2:")
for i in range(2):
    for j in range(2):
        m2[i][j]  = int(input("[{:d}, {:d}]: ".format(i+1,j+1)))

print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print(m1[i][j],end=" ")
    print()

print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(m2[i][j],end=" ")
    print()

print("Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        print(m1[i][j]+m2[i][j],end=" ")
    print()