import numpy as np
# 使用random.randint方向產生5x4矩陣，再用np方向求解
matrix = np.random.randint(1,21,20)
print("隨機正整數:",matrix)
matrix = matrix.reshape(5,4)
print("Matrix:\n",matrix)
print("max:",matrix.max())
print("min:",matrix.min())
print("mean:",matrix.mean())
print("sum:",matrix.sum())
print("std:",matrix.std())
print("Four corners:\n",matrix[np.ix_([0,4],[0,3])])