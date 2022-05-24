# TODO
num = eval(input())
for i in range(num):
    date = input().split()
    date = [eval(i) for i in date]
    date.sort()
    print("{:.2f}".format(date[-1] - date[0]))

num = int(input())
for i in range(num):
    data = input().split()
    data = [eval(i) for i in data]
    data.sort()
    print("{:.2f}".format(data[-1] - data[0]))
