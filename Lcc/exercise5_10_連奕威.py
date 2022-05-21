"""
練習：輸入欲產生的個數,之後依序輸入其個數存於串列
將此串列排序後,轉為數組與集合,分別印出。
"""

input_count = int(input("請輸入要產生的個數：\n"))
answer = []

for i in range(1, input_count + 1):
    num = eval(input("請輸入第{}個數字".format(i)))
    answer.append(num)

new_answer = sorted(answer)

print("tuple型態：{}".format(tuple(new_answer)))
print("list型態：{}".format(new_answer))
print("set型態：{}".format(set(new_answer)))
