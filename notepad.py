from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import font, simpledialog
file=None
if __name__ == '__main__':

    root=Tk()

    #function for  new file
    def newfile():
        global file
        root.title("untitled-1")
        file=None
        textarea.delete(1.0,END) #The deletion of first charcter of first line till end

    #function for open file
    def openfile():
        global file
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + "-Notepad")
            textarea.delete(1.0, END)
            f = open(file, "r")
            textarea.insert(1.0, f.read())
            f.close()

    #function for a new window
    def a_new_window():
        global file
        root.title("Untitled")
        file=None
        textarea.delete(1.0,END)

    #function for save file
    def savefile():
        global file
        if file is None:
            savefile_as()
        else: #save the file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-notepad")
            print("file is saved")

    #function for save file as
    def savefile_as():
        global file
        if file is None:
            file = asksaveasfilename(initialfile="hamna.txt", defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:  # save as the file
                f = open(file, "w")
                f.write(textarea.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + "-notepad")
                print("filed is being saved")

        else:  # save the file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-notepad")
            print("file is being saved")

    #function for copy
    def copy():
        textarea.event_generate(("<<Copy>>"))

    #function for cut
    def cut():
        textarea.event_generate(("<<Cut>>"))

    #function for paste
    def paste():
        textarea.event_generate(("<<Paste>>"))

    #function for replace
    def replace():
        find_text = simpledialog.askstring("Find", "Enter text to replace")
        replace_text = simpledialog.askstring("Replace", "Enter replacement text")
        if find_text and replace_text:
            content = textarea.get(1.0, END)
            new_content = content.replace(find_text, replace_text)
            textarea.delete(1.0, END)
            textarea.insert(1.0, new_content)

    #function for add  font
    def add_font():
        list=font.families()
        choose=simpledialog.askstring("choose a font","enter a font name")
        if choose in font.families():
            textarea.config(font=(choose,20))
            print(f"{choose}")
        else:
            print("not valid")

    #function for send a feedback
    def send_fd():
        user_feedback=simpledialog.askstring("user feedback","user views")
        print(f"{user_feedback}")

    #function for about
    def about():
       showinfo("Notepad", "made by hamna . Student of software engineering")

    size=14

    #function for zoom in
    def Zoom_in():
        global size
        size=size+2
        print(f"{size}")
        textarea.config(font=("Times New Roman",size))

    #function for zoom out
    def Zoom_out():
        global size
        size=size-2
        print(f"{size}")
        textarea.config(font=("Times New Roman", size))

    #function for restore
    def Restore():
        global size
        size-14
        print(f"{size}")
        textarea.config(font=("Times New Roman", size))

    root.title("untitled")
    root.geometry("600x700")
    textarea=Text(root,font=("Times New Roman",14))
    textarea.pack(expand=True, fill=BOTH)
    file=None #no file is being created
    menubar=Menu(root)

    #file
    filemenu=Menu(menubar,tearoff=-0)
    filemenu.add_command(label="New",command=newfile)
    filemenu.add_command(label="Open",command=openfile)
    filemenu.add_command(label="New window", command=a_new_window)
    filemenu.add_separator()
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_command(label="save as",command=savefile_as)
    menubar.add_cascade(label="file",menu=filemenu)

    #edit
    editmenu=Menu(menubar, tearoff=0)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_separator()
    editmenu.add_command(label="Paste", command=paste)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_separator()
    editmenu.add_command(label="Replace",command=replace)
    menubar.add_cascade(label="Edit",menu=editmenu)

    #format
    formatmenu=Menu(menubar,tearoff=0)
    formatmenu.add_command(label="Font",command=add_font)
    menubar.add_cascade(label="Format" , menu=formatmenu)

    #help
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="Send feedback",command=send_fd)
    helpmenu.add_separator()
    helpmenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)

    #view
    view_menu=Menu(menubar,tearoff=0)
    view_menu.add_command(label="Zoom in", command=Zoom_in)
    view_menu.add_command(label="Zoom out", command=Zoom_out)
    view_menu.add_command(label="Restore size", command=Restore)
    menubar.add_cascade(label="View",menu=view_menu)
    root.config(menu=menubar)

    #scroll bar
    scroll=Scrollbar(textarea) #scroll bar in parent widget
    scroll.pack(side=RIGHT,fill=Y) #scroll bar to right of parent widget and fills to y axis
    scroll.config(command=textarea.yview) #the scroll bar is configured to the y axis of the parent widget
    textarea.config(yscrollcommand=scroll.set) #the scroll bar is then setted in the parent widget

root.mainloop()