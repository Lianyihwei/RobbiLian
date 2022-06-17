# TODO

times = eval(input())

for j in range(times):
    num = input()
    sum = 0
    for i in num:
        sum += eval(i)
    print("Sum of all digits of {} is {}".format(num,sum))
