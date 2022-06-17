# TODO

evc = 0
odc = 0
for i in range(10):
    num = eval(input())
    if num %2 == 0:
        evc += 1
    else:
        odc += 1
print("Even numbers:",evc)
print("Odd numbers:",odc)
