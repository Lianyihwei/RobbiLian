# TODO
setx = set()
sety = set()

print("Enter group X's subjects:")
while True:
    x = input()
    if x == "end":
        break
    setx.add(x)

print("Enter group Y's subjects:")
while True:
    y = input()
    if y == "end":
        break
    sety.add(y)

print(sorted(setx | sety))
print(sorted(setx & sety))
print(sorted(sety - setx))
print(sorted(setx ^ sety))
