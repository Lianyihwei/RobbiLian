'''
輸出說明
請用numpy隨機產生5~15之間，15個正整數並輸出
請將 1. 轉成3×5的X矩陣並輸出
請輸出X矩陣的最大值
請輸出X矩陣的最小值
請輸出X矩陣的總和
請輸出X矩陣四個角落的元素內容
'''

# --開始--批改評分使用，請勿變動
set_seed = 123
# --結束--批改評分使用，請勿變動

import numpy as np

x = np.random.RandomState(set_seed).randint(low=5, high=16, size=15)
print('隨機正整數：', x)

x = x.reshape(3, 5)
print('X矩陣內容：')
print(x)
print('最大：', np.max(x))
print('最小：', np.min(x))
print('總和：', np.sum(x))
print('四個角落元素：')
print(x[np.ix_([0, 2], [0, 4])])
