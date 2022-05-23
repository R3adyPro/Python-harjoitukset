import random
import string

password_charecters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#£$¤%&/=?*')

def password_generator():
    lenght = input('Choose the lenght of the password. ')
    password = []
    for i in range(int(lenght)):
        password.append(random.choice(password_charecters))
    print("".join(password))

password_generator()
