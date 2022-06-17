# TODO
set1 = set()
set2 = set()
set3 = set()

print("Input to set1:")
for i in range(5):
    num = eval(input())
    set1.add(num)
# TODO
print("Input to set2:")
for i in range(3):
    num = eval(input())
    set2.add(num)
# TODO
print("Input to set3:")
for i in range(9):
    num = eval(input())
    set3.add(num)
# TODO
print(set3.issuperset())
print(set2.issubset())

print("set2 is subset of set1:",set2.issubset(set1))
print("set3 is superset of set1:",set3.issuperset(set1))
