from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc

def delete_book():
    bid = book_Info1.get()

    delete_SQL = "DELETE FROM "+book_Table+" WHERE bid = '"+bid+"'"
    print(delete_SQL)
    delete_issued = "DELETE FROM "+issue_Table+" WHERE bid = '"+bid+"'"
    print(delete_issued)

    try:
        cursor.execute(delete_SQL)
        conn.commit()
        cursor.execute(delete_issued)
        conn.commit()

        messagebox.showinfo("Book deleted")

    except:
        messagebox.showinfo("Book not deleted")
    
    print(bid)

    book_Info1.delete(0,END)
    root.destroy()


def delete():
    global book_Info1,book_Info2,book_Info3,book_Info4,conn,cursor,book_Table,root,Canvas,issue_Table

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
    
    cursor = conn.cursor()

    # name of the table here
    book_Table = 'books'
    issue_Table = "books_issued"

    Canvas1 = Canvas(root)
    Canvas1.config(bg='black')
    Canvas1.pack(expand=True,fill=BOTH)

    heading_Frame1 = Frame(root,bg='#ff6e40',bd=5,relief = RAISED,cursor='target')
    heading_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    heading_Label = Label(heading_Frame1,text='Add Books',bg='black',fg='red',font=('Courier',15))
    heading_Label.place(relx=0,rely=0,relwidth=1,relheight=1)

    label_Frame = Label(root,bg='black',relief = RAISED)
    label_Frame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.5)

    label_Frame1 = Label(label_Frame,text="Book ID :- ",bg='black',fg='white')
    label_Frame1.place(relx=0.05,rely=0.5)

    book_Info1 = Entry(label_Frame)
    book_Info1.place(relx=0.3,rely=0.5,relwidth=0.62)

    # Button for Sbumit
    Submit_button = Button(root,text="SUBMIT",bg='#d1ccc0',fg='black',command=delete_book) # add command
    Submit_button.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)

    # Button for Quit
    quit_button = Button(root,text="Quit",bg='#f7f1e3',fg='black',command = root.destroy) # add command
    quit_button.place(relx=0.5,rely=0.9,relwidth=0.18,relheight=0.08)

    root.mainloop()