import random

print("RANDOM PASSWORD GENERATOR IN PYTHON")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&"

while 1:
    password_len = int(input("Please Enter Password Length :"))
    password_count = int(input("How Many Password Do You Want :"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Generated Password :",password)
        