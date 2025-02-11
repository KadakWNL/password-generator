import random
import string

def password_gen():
    number_of_characters = random.randint(8,12)
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
    password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice("!@#$%^&*")
    for i in range(number_of_characters-4):
        password += random.choice(chars)
    random.shuffle(list(password))
    return password

print(password_gen())