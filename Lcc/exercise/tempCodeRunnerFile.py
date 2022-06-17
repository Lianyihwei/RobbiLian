import numpy as np
# 使用random.randint方向產生5x4矩陣，再用np方向求解
matrix = np.random.randint(0,21,(5,4))
print(matrix)
print(matrix.max())
print(matrix.min())
print(matrix.mean())
print(matrix.sum())
print(matrix.std())
print(matrix[[0,0,4,4],[0,3,0,3]])