import os
print("saving file to:", os.getcwd())
from tkinter import *
root = Tk()
root.geometry("100x150")
root.config(bg="grey")
root.title("PASSWORD GENERATOR AND STRENGTH CHECKER")
title=Label(root, text="AUTOMATIC PASSWORD GENERATOR AND STRENGTH CHECKER",font=("Times New Roman",16,"bold"))
title.grid(row=1, column=6)
import random
from string import digits,ascii_letters,punctuation
passcode=""
length=12

user_password=StringVar()

#password generation
def generate_password():
    global passcode
    characters = digits + ascii_letters + punctuation
    passcode = "".join(random.choice(characters) for _ in range (length))
    user_password.set(passcode)

#entry of password widget and label
password = Label(root, text="ENTRY OF PASSWORD",font=("Times New Roman",12,"italic"))
password.grid(row=3, column=1)
entry_password=Entry(root,textvariable=user_password)
entry_password.grid(row=3,column=2)
b1=Button(root,fg="white", bg="black", text="generate password", font=("Arial", 9, "bold"),command=generate_password)
b1.grid(row=4,column=2)

#strong password
pass1=list(passcode)
strength_password=StringVar()
def stronger_password():
    has_digits=any(ch in digits  for ch in passcode)
    has_alphabets=any(ch in ascii_letters  for ch in passcode)
    has_punctuation=any(ch in  punctuation for ch in passcode)
    if has_digits==True and has_alphabets==True and has_punctuation==True :
        strength_password.set("strong")
    else:
        strength_password.set("weak")

    #Handling passwords by storing it in a file
    with open("passwords.txt", "a") as file:
        file.write(f"{passcode}\t{strength_password.get()}\n")

#strength checker label and widget
b2=Label(root,text="STRENGTH CHECKER",font=("Times New Roman",12,"italic"))
b2.grid(row=5,column=1)
b2_text=Entry(root,textvariable=strength_password)
b2_text.grid(row=5,column=2)
b3=Button(root,text="Strength Check",bg="black",fg="white",font=("Arial", 9, "bold"),command=stronger_password)
b3.grid(row=6,column=2)
root.mainloop()