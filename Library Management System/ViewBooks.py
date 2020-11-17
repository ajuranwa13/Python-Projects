from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc

# making connection wth sql server
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-9O99F71M\SQLEXPRESS;'
    'Database=library;'
    'Trusted_Connection=yes;'
    )

cursor = conn.cursor()

book_Table = "books"

# function to view all books 
def View():

    root = Tk()
    root.title("Library")
    root.minsize(width=450,height=450)
    root.geometry('700x700')

    Canvas1 = Canvas(root)
    Canvas1.config(bg='black')
    Canvas1.pack(expand=True,fill=BOTH)

    heading_Frame1 = Frame(root,bg='#ff6e40',bd=5,relief = RAISED,cursor='target')
    heading_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    heading_Label = Label(heading_Frame1,text='View Books',bg='black',fg='red',font=('Courier',15))
    heading_Label.place(relx=0,rely=0,relwidth=1,relheight=1)

    label_Frame = Label(root,bg='black',relief = RAISED)
    label_Frame.place(relx=0.1,rely=0.4,relwidth=0.83,relheight=0.4)
    y = 0.25

    Label(label_Frame,text="%-10s%-40s%-30s%-10s"%('BID','Title','Author','Status'),bg="black",fg="white").place(relx=0.07,rely=0.1)
    Label(label_Frame,text="-------------------------------------------------------------------",bg="black",fg="white").place(relx=0.05,rely=0.2)

    get_books = "SELECT * FROM books"

    try:
        cursor.execute(get_books)

        for i in cursor.fetchall():
            Label(label_Frame,text="%-10s%-30s%-30s%-10s"%(i[0],i[1],i[2],i[3]),bg="black",fg="white").place(relx=0.07,rely=y)
            y +=0.1

    except:
        messagebox.showinfo('Failed to fatch data from database')

    quit_button = Button(root,text="Quit",bg='#f7f1e3',fg='black',command = root.destroy) # add command
    quit_button.place(relx=0.5,rely=0.9,relwidth=0.18,relheight=0.08)
    
    root.mainloop()
