
# PASSWORD MANAGER

# This code generates the password of hard level

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':',';','<',',','>','.','/','?']

print('WELCOME TO PASSWORD MANAGER! //Generared by BADHANN')

pass_letter = int(input("Enter the number of letters need to be in password: "))
pass_number = int(input("Enter the number of numbers need to be in password: "))
pass_symbol = int(input("Enter the number of symbols need to be in password: "))

pass_list = []
for char in range(0,pass_letter):
    pass_list += random.choice(letters)

for num in range(0,pass_number):
    pass_list += random.choice(numbers)

for sym in range(0,pass_symbol):
    pass_list += random.choice(symbols)

# print(pass_list)
random.shuffle(pass_list)
# print(pass_list)

password = ''
for char in pass_list:
    password += char

print("The generated password is: " + password)