letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [ '!','#','$','%','&','(',')','*','+']

print("Welcome to Random password Generator!")
lt_num = int(input("Please Enter number of letters for password: "))
nr_sym = int(input("Please Enter number of symbols to be added: "))
pss_num = int(input("Please Enter how many numbers to be included in password: "))

import random as rd

#Easy Level

# password =""

# for char in range(0,lt_num):
#     password+=rd.choice(letters)

# for char in range(0,nr_sym):
#     password+=rd.choice(symbols)

# for char in range(0,pss_num):
#     password+=rd.choice(numbers)

# print(f"Your Password is : {password}")

#Hard Level

password_list = []

for char in range(0,lt_num):
    password_list.append(rd.choice(letters))

for char in range(0,nr_sym):
    password_list.append(rd.choice(symbols))

for char in range(0,pss_num):
    password_list.append(rd.choice(numbers))

str2=""
# print(password_list)
rd.shuffle(password_list)
# print(password_list)

for final_pass in password_list:
    str2 +=final_pass

print(f"Your password is: {str2}")