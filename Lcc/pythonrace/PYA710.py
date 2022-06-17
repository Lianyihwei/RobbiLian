#TODO
from tabnanny import check


dict = {}
while True:
    key = input("Key: ")
    if key == "end":
        break
    value = input("Value: ")
    dict[key] = value

search_key = input("Search key: ")
print(search_key in dict.keys())