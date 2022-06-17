# TODO

password = input()

if (len(password) <= 7) or (password.isalnum() !=True)  or password.islower():
    print("Invalid password")
else:
    print("Valid password")
