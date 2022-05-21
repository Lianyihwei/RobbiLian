# TODO
num_list = []
for i in range(4):
    num = int(input())
    num_list.append(num)


# 向右靠齊
# TODO
print("|{:5d} {:5d}|".format(num_list[0], num_list[1]))
print("|{:5d} {:5d}|".format(num_list[2], num_list[3]))
# 向左靠齊
# TODO
print("|{:<5d} {:<5d}|".format(num_list[0], num_list[1]))
print("|{:<5d} {:<5d}|".format(num_list[2], num_list[3]))
