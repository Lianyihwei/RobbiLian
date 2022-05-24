f_name = input()
str_old = input()
str_new = input()
with open(f_name) as f:
    data = f.read()

print("=== Before the replacement")
print(data)
print("=== After the replacement")
data = data.replace(str_old,str_new)
print(data)
