
import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
         'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&']

print('welcome to password generator')
nr_letters=int(input('how many letters would you like in password'))
nr_numbers=int(input('how many numbers would you like in password'))
nr_symbols=int(input('how many symbols in passsword'))

password_list=[]
for x in range(nr_numbers+1):
    password_list+=random.choice(letters)

for x in range(nr_numbers+1):
    password_list+=random.choice(numbers)

for x in range(nr_symbols+1):
    password_list+=random.choice(symbols)



random.shuffle(password_list)
pasword=""
for x in password_list:
    pasword+=x

print(pasword)