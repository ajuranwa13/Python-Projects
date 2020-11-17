from tkinter import *
from PIL import ImageTk,Image
import pyodbc
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# let's connect this file with my database
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-9O99F71M\SQLEXPRESS;'
    'Database=library;'
    'Trusted_Connection=yes;'
)

# now we will draw gui to library 
root = Tk()
root.title('My Home Library')
root.minsize(width=450,height=450)
root.geometry('700x700')

# Addinng a backgroung image
same = True
n = 0.25

backgroung_image = Image.open(open("E:\Python projects\Library Management System\lib.jpg", 'rb'))
[imageSizeWidth,imageSizeHeight] = backgroung_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

# Image.ANTIALIAS (a high-quality downsampling filter image returns)
backgroung_image = backgroung_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(backgroung_image)

#Canvas is your GUI screen in which you can place items.
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)
Canvas1.config(bg='white',width=newImageSizeWidth,height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

# writing a head frame msg
heading_frame1 = Frame(root,bg='black',bd=5,relief = RAISED,cursor='spider')
heading_frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

heading_Label = Label(heading_frame1,text='Welcome to my Own Library',bg='black',fg='white',font=('Courier',15))
heading_Label.place(relx=0,rely=0,relwidth=1,relheight=1)

# adding buttons on the opening window
button_1 = Button(root,text='Add Book Details',bg='black',fg='red',command=addBook)
button_1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)

button_2 = Button(root,text='Delete Book',bg='black',fg='red',command=delete)
button_2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)

button_3 = Button(root,text='View Book List',bg='black',fg='red',command=View)
button_3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)

button_4 = Button(root,text='Issue Book To Student',bg='black',fg='red',command=issue_book)
button_4.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)

button_5 = Button(root,text='Return Book',bg='black',fg='red',command=return_Book)
button_5.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)

root.mainloop()