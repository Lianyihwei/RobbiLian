x = []
while True:
    num = eval(input())
    if num == 9999:
        break
    x.append(num)
print(min(x))