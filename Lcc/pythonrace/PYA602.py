# TODO

sum = 0

for i in range(5):
    pok = input()
    if pok == "A":
        sum += 1
    elif pok == "J":
        sum += 11
    elif pok == "Q":
        sum += 12
    elif pok == "K":
        sum += 13
    else:
        sum += int(pok)
print(sum)
