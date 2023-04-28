import string
import random

def passwordGenerator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passwordLength = int(input("Enter the length of the password: "))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    password = ("".join(s[0:passwordLength]))
    print(password)
passwordGenerator()