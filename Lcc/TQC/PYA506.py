# TODO
def computer(a, b, c):
    delta = b**2 - (4 * a * c)
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        ans1 = (-b + (b**2 - (4 * a * c)) ** (0.5)) / (2 * a)
        ans2 = (-b - (b**2 - (4 * a * c)) ** (0.5)) / (2 * a)
        return str(ans1) + ", " + str(ans2)


a = eval(input())
b = eval(input())
c = eval(input())
answer = computer(a, b, c)
if answer == None:
    print("Your equation has no root.")
else:
    print(answer)
