"""
練習：輸入欲產生的個數,之後依序輸入其個數存於串列
將此串列排序後,轉為數組與集合,分別印出。
"""

input_count = eval(input("請輸入要產生的個數：\n"))
list = ""

for i in input_count:
    num = eval(input("請輸入第{}個數字".format(i)))
    list += num
print(list)
