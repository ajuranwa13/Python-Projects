from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc


# we will create fun to add book's frames and labels 
def addBook():
    global book_Info1,book_Info2,book_Info3,book_Info4,conn,book_Table,root

    root = Tk()
    root.title("Library")
    root.minsize(width=450,height=450)
    root.geometry('700x700')

    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=LAPTOP-9O99F71M\SQLEXPRESS;'
        'Database=library;'
        'Trusted_Connection=yes;'
        )

    # name of the table here
    book_Table = 'books'

    Canvas1 = Canvas(root)
    Canvas1.config(bg='black')
    Canvas1.pack(expand=True,fill=BOTH)

    heading_Frame1 = Frame(root,bg='#ff6e40',bd=5,relief = RAISED,cursor='target')
    heading_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    heading_Label = Label(heading_Frame1,text='Add Books',bg='black',fg='red',font=('Courier',15))
    heading_Label.place(relx=0,rely=0,relwidth=1,relheight=1)

    label_Frame = Label(root,bg='black',relief = RAISED)
    label_Frame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # label for book id
    label1 = Label(label_Frame,text='Book ID : ',bg='black',fg='white')
    label1.place(relx=0.05,rely=0.2,relheight=0.08)

    book_Info1 = Entry(label_Frame)
    book_Info1.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)

    # label for Title
    label2 = Label(label_Frame,text='Title : ',bg='black',fg='white')
    label2.place(relx=0.05,rely=0.35,relheight=0.08)

    book_Info2 = Entry(label_Frame)
    book_Info2.place(relx=0.3,rely=0.35,relwidth=0.62,relheight=0.08)

    # label for Author
    label3 = Label(label_Frame,text='Author : ',bg='black',fg='white')
    label3.place(relx=0.05,rely=0.50,relheight=0.08)

    book_Info3 = Entry(label_Frame)
    book_Info3.place(relx=0.3,rely=0.50,relwidth=0.62,relheight=0.08)

    # label for Status
    label4 = Label(label_Frame,text='Status : ',bg='black',fg='white')
    label4.place(relx=0.05,rely=0.65,relheight=0.08)

    book_Info4 = Entry(label_Frame)
    book_Info4.place(relx=0.3,rely=0.65,relwidth=0.62,relheight=0.08)

    # Button for Sbumit
    Submit_button = Button(root,text="SUBMIT",bg='#d1ccc0',fg='black',command = book_Register) # add command
    Submit_button.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)

    # Button for Quit
    quit_button = Button(root,text="Quit",bg='#f7f1e3',fg='black',command = root.destroy) # add command
    quit_button.place(relx=0.5,rely=0.9,relwidth=0.18,relheight=0.08)

    root.mainloop()


# now fun for addind data in tables
def book_Register():

    bid = book_Info1.get()
    title = book_Info2.get()
    author = book_Info3.get()
    status = book_Info4.get()
    status = status.lower()

    cursor = conn.cursor()

    SQLCommand = ("INSERT INTO books(bid,title,author,status) VALUES (?,?,?,?)")
    values = (bid,title,author,status)
    try:
        cursor.execute(SQLCommand,values)
        conn.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo('Error',"Book not added ")

    
    print(bid,title,author,status)
    conn.close()

    
