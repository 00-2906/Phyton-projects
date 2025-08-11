import random
from string import digits,ascii_letters,punctuation
passcode=" "
def input_password():
    global passcode
    choice="Y"
    password_length=12
    choice=input("do you want a system generated password:").lower()
    if(choice=="y"):
        characters=digits+ascii_letters+punctuation
        for _ in range(password_length):
            passcode+=random.choice(characters)
    else:
        user_digits=input("enter digits in password:")
        user_alphabets=input("enter alphabets in password:")
        user_punctuation=input("enter punctuation in password:")
        characters=user_digits+user_alphabets+user_punctuation
        if(len(characters) ==12):
            passcode=characters
        else:
            print("meet the required number of elements")
    print("password generated:",passcode)


def stronger_password(passcode):
    print("----------- STRONGER PASSWORD------------")
    password=list(passcode)
    print(password)
    for c in range(len(password)):
        has_digits=any(c in digits  for c in passcode)
        has_alphabets=any(c in ascii_letters  for c in passcode)
        has_punctuation=any(c in  punctuation for c in passcode)
    print("digits:",has_digits)
    print("alphabets:",has_alphabets)
    print("punctuation:",has_punctuation)
    if(has_digits== True and has_alphabets== True and has_punctuation== True):
        print("strong password")
    else:
        print("not a strong password. Generate again")
input_password()
stronger_password(passcode)