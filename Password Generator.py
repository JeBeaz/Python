import random
import string
from string import punctuation

while True:
    print('Password Generator')
    alphabet = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list(string.punctuation)
    characters = list(string.ascii_letters + string.digits + string.punctuation)

    #How Many Passwords we Want to Make
    number = input('Amount of Passwords Needed:')
    number = int(number)

    #How Long We Want our Passwords to Be
    length = input('How Long Do You Want Your Password:')
    length = int(length)

    #Shows Password Created
    print('Here is Your Password List:')

    for pwd in range(number):
        password = ''
        for c in range(length):
            password += random.choice(characters)
        print(password)
    
    another_passowrd = input('Want Another Password? (y/n):')
    if another_passowrd.lower() != 'y':
        break
#this is a test for source control