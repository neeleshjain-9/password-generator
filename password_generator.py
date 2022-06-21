import string
import random
print()
print()

print("Welcome to the PyPassword Generator")
l = int(input("How many letters would you like? "))
s = int(input("How many symbols would you like? "))
n = int(input("How many numbers would you like? "))

letters = random.choices(string.ascii_letters, k=l)
symbols = random.choices(string.punctuation, k=s)
numbers = random.choices(string.digits, k=n)

password_list = letters + symbols + numbers

password_new = random.shuffle(password_list)
password = "".join(password_list)

print()
print()
