from tkinter import *

root = Tk()
root['bg'] = '#292929'
root.title("Discord name for play")
root.geometry('350x90')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.resizable(False, False)

def show_rename():
     root.title(name.get())

name = StringVar()

name_entry = Entry(textvariable=name, font=('Arial',18, 'bold'), bg='#202020', fg='#ffffff')
name_entry.place(relx=.0, rely=.0, width=349, height=30)

name_button = Button(text="Rename", command=show_rename, font=('Arial',18), bg='#202020', fg='#ffffff')
name_button.place(relx=.0, rely=.4, width=100, height=50)

root.mainloop()