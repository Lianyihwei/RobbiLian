# TODO
time = eval(input())

for i in range(time):
    check = set(input().lower())
    check.remove(" ")
    print(len(check)==26)

