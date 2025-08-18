from tkinter import *
import math
root=Tk()
root.geometry("500x200")
root.title("Calculator by Hamna")
root.config(bg="black")

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if(text=="="):
        value=scvalue.get()
        if value.isdigit():
            value=int(scvalue.get())
        else:
            value = eval(value, {"__builtins__": None}, {
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "log": math.log,
                "sqrt":math.sqrt,
                "e":math.e,
            })
        scvalue.set(value)
        screen.update()
    elif(text=="C"):
        scvalue.set(" ")
        screen.update()
    elif(text=="del"):
        current = scvalue.get()  # get the string from StringVar
        if current:  # only delete if not empty
            scvalue.set(current[:-1])  # remove last character
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    return event

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font=("Times New Roman",50,"bold"))
screen.pack(padx=30,pady=40)

f1=Frame(root,bg="grey")
b1=Button(f1,text="9",font=("Times New Roman",30,"bold")) # buttond from 9-0
b1.pack(side=LEFT,padx=30,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="8",font=("Times New Roman",30,"bold"))
b2.pack(side=LEFT,padx=30,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="7",font=("Times New Roman",30,"bold"))
b3.pack(side=LEFT,padx=30,pady=10)
b3.bind("<Button-1>",click)
b4=Button(f1,text="6",font=("Times New Roman",30,"bold"))
b4.pack(side=LEFT,padx=30,pady=10)
b4.bind("<Button-1>",click)
f1.pack()

f2=Frame(root,bg="grey")
b5=Button(f2,text="5",font=("Times New Roman",30,"bold"))
b5.pack(side=LEFT,padx=30,pady=10)
b5.bind("<Button-1>",click)
b6=Button(f2,text="4",font=("Times New Roman",30,"bold"))
b6.pack(side=LEFT,padx=30,pady=10)
b6.bind("<Button-1>",click)
b7=Button(f2,text="3",font=("Times New Roman",30,"bold"))
b7.pack(side=LEFT,padx=30,pady=10)
b7.bind("<Button-1>",click)
b8=Button(f2,text="2",font=("Times New Roamn",30,"bold"))
b8.pack(side=LEFT,padx=30,pady=10)
b8.bind("<Button-1>",click)
f2.pack()

f3=Frame(root,bg="grey")
b9=Button(f3,text="1",font=("Times New Roman",30,"bold"))
b9.pack(side=LEFT,padx=30,pady=10)
b9.bind("<Button-1>",click)
b10=Button(f3,text="0",font=("Times New Roman",30,"bold"))
b10.pack(side=LEFT,padx=30,pady=10)
b10.bind("<Button-1>",click)
b11=Button(f3,text="=",font=("Times New Roamn",30,"bold")) #button of {=}
b11.pack(side=LEFT,padx=30,pady=10)
b11.bind("<Button-1>",click)
b12=Button(f3,text="C",font=("Times New Roman",30,"bold")) #button for clear
b12.pack(side=LEFT,padx=30,pady=10)
b12.bind("<Button-1>",click)
f3.pack()

f4=Frame(root,bg="grey")
b13=Button(f4,text="+",font=("Times New Roman",30,"bold")) #button for +
b13.pack(side=LEFT,padx=30,pady=10)
b13.bind("<Button-1>",click)
b14=Button(f4,text="-",font=("Times New Roamn",30,"bold")) #button for -
b14.pack(side=LEFT,padx=30,pady=10)
b14.bind("<Button-1>",click)
b15=Button(f4,text="*",font=("Times New Roman",30,"bold")) #button for *
b15.pack(side=LEFT,padx=30,pady=10)
b15.bind("<Button-1>",click)
b16=Button(f4,text="/",font=("Times New Roman",30,"bold")) #button for /
b16.pack(side=LEFT,padx=30,pady=10)
b16.bind("<Button-1>",click)
f4.pack()

f5=Frame(root,bg="grey")
b17=Button(f5,text="sin",font=("Times New Roamn",30,"bold")) #button for sine
b17.pack(side=LEFT,padx=20,pady=10)
b17.bind("<Button-1>",click)
b18=Button(f5,text="cos",font=("Times New Roman",30,"bold")) #button for cos
b18.pack(side=LEFT,padx=30,pady=10)
b18.bind("<Button-1>",click)
b19=Button(f5,text="tan",font=("Times New Roman",30,"bold")) #button for tan
b19.pack(side=LEFT,padx=30,pady=10)
b19.bind("<Button-1>",click)
b20=Button(f5,text="sqrt", font=("Times New Roman",30,"bold")) #button for square root
b20.pack(side=LEFT,padx=30,pady=10)
b20.bind("<Button-1>",click)
f5.pack()

f6=Frame(root,bg="grey")
b21=Button(f6,text="log",font=("Times New Roman",30,"bold")) #button for log
b21.pack(side=LEFT,padx=30,pady=10)
b21.bind("<Button-1>",click)
b22=Button(f6,text="e",font=("Times New Roman",30,"bold")) #button for exponential
b22.pack(side=LEFT,padx=30,pady=10)
b22.bind("<Button-1>",click)
b23=Button(f6,text="**",font=("Times New Roman",30,"bold")) #button for power to any number
b23.pack(side=LEFT,padx=30,pady=10)
b23.bind("<Button-1>",click)
b24=Button(f6,text="del",font=("Times New Roman",30,"bold")) #button of del to remove the last digit
b24.pack(side=LEFT,padx=30,pady=10)
b24.bind("<Button-1>",click)
f6.pack()

f7=Frame(root,bg="grey")
b25=Button(f7,text="(",font=("Times New Roman",30,"bold")) #button for brackets
b25.pack(side=LEFT,padx=30,pady=10)
b25.bind("<Button-1>",click)
b26=Button(f7,text=")",font=("Times New Roman",30,"bold"))
b26.pack(side=LEFT,padx=30,pady=10)
b26.bind("<Button-1>",click)
f7.pack()
root.mainloop()