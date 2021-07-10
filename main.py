import random as r

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to Password Generator")
l = int(input("How many letters do you want in your password: "))
n = int(input("How many numbers do you want in your password: "))
s = int(input("How many symbols do you want in your password: "))
for char in range(0, l):
    password.append(r.choice(letters))
for num in range(0, n):
    password.append(r.choice(numbers))
for char in range(0, s):
    password.append(r.choice(symbols))
r.shuffle(password)
final_password = ""
for i in password:
    final_password += i
print(f'Your Password is: {final_password}')
