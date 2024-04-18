import random 

print("this is your password: ")

chars = 'abcderfgijklmnopqrstuvwyz12345678910!@#$%*ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = ''

for x in range(20):
    password += random.choice(chars)

print(password)
