import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from database import Table
from Cartesiantree import CartesianTree
from Cartesiantree import Node
data=Table()
value=data.read('data/books.csv','serial')
cat=CartesianTree(data.keys,0,len(data.keys)-1,data.records)
def show_frame(frame):
    frame.tkraise()
    

window= tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)



frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window) # search and delete
frame4 = tk.Frame(window) #insert


for frame in (frame1, frame2, frame3,frame4):
    frame.grid(row=0,column=0,sticky='nsew')
#==================Frame 2 code
def view1():
    def delete():
        tree.destroy()
        hsb.destroy()
    lst=cat.inorder()
    tree=ttk.Treeview(frame2)
    s=ttk.Style(frame2)
    count=0
    for i in lst:
        tree.insert('',count,text="",values=(i,lst[i][0],lst[i][1],lst[i][2],lst[i][3]))
        count+=1
    frame2_btn = tk.Button(frame2, text='Wapsi',command=lambda:[show_frame(frame1),delete()])
    frame2_btn.pack(fill='x', ipady=15)
    s.theme_use('clam')
    s.configure(".",font=('Helvetice',11))
    s.configure("Treeview.Heading",foreground='black',font=('Times New Roman',15))
    hsb=ttk.Scrollbar(frame2,orient='vertical')
    hsb.configure(command=tree.yview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)
    tree['columns']=("ISBN","Name","Category","Price","Pages")
    tree.column("ISBN",width=500,anchor=CENTER)
    tree.column("Name",width=100,anchor=CENTER)
    tree.column("Category",width=100,anchor=CENTER)
    tree.column("Price",width=100,anchor=CENTER)
    tree.column("Pages",width=100,anchor=CENTER)
    tree.heading("ISBN",text="ISBN",anchor=CENTER)
    tree.heading("Name",text="Name",anchor=CENTER)
    tree.heading("Category",text="Category",anchor=CENTER)
    tree.heading("Price",text="Price",anchor=CENTER)
    tree.heading("Pages",text="Pages",anchor=CENTER)
    tree['show']='headings'
    tree.pack()
#==================Frame 1 code


background = Canvas(frame1,height = 200, width = 200)
img = PhotoImage(file="wp.png")
background_label = Label(frame1,image=img,bg="pink")
background_label.place(x=0,y=0,relwidth=1, relheight=1)
background.pack()

img2 = PhotoImage(file="pretty books.png")
Label(frame1,image=img2,bg="pink").place(x=50,y=150)

Heading=Label(frame1,text='Fries Library Management System',fg='DeepPink4',bg='LightPink1',font=('Times New Roman',24,'bold'))

Heading.pack() #print on the screen
Heading.place(x=400,y=20)

isbn=Label(frame1,text='ISBN ',fg='black',bg='#fff0f5')
isbn.pack(pady=(20,5))
isbn.place(x=500,y=200)

isbn_input=Entry(frame1,width=50)#text input on screen
isbn_input.pack(ipady=4,pady=(10,5)) #ipady for height
isbn_input.place(x=600,y=200)

frame1_btn = tk.Button(frame1, text='View',fg="black",bg="PaleTurquoise",font=('Times New Roman',24,'bold'),command=lambda:[show_frame(frame2),view1()])
frame1_btn.pack(ipady=15)
frame1_btn.place(x=600,y=300)

search_btn = tk.Button(frame1, text='Search',fg="black",bg="PaleTurquoise",font=('Times New Roman',24,'bold'),command=lambda:show_frame(frame3))
search_btn.pack(ipady=15)
search_btn.place(x=600,y=600)

insert_btn = tk.Button(frame1, text='Insert',fg="black",bg="PaleTurquoise",font=('Times New Roman',24,'bold'),command=lambda:show_frame(frame4))
insert_btn.pack(ipady=15)
insert_btn.place(x=600,y=400)


window.title('Fries Management System') # heading of the window
window.iconbitmap('icon.ico') #icon of the window

#==================Frame 3 code
def search_func():
    value=search_input.get()
    print("New Key: ",value)
    ans=cat.search(value)
    
    tree1=ttk.Treeview(frame3)
    s1=ttk.Style(frame3)
    count=0
    tree1.insert('',count,text="",values=(value,ans[0],ans[1],ans[2],ans[3]))
    s1.theme_use('clam')
    s1.configure(".",font=('Helvetice',11))
    s1.configure("Treeview.Heading",foreground='black',font=('Times New Roman',15))
    hsb1=ttk.Scrollbar(frame2,orient='vertical')
    hsb1.configure(command=tree1.yview)
    tree1.configure(xscrollcommand=hsb1.set)
    hsb1.pack(fill=Y,side=RIGHT)
    tree1['columns']=("ISBN","Name","Category","Price","Pages")
    tree1.column("ISBN",width=500,anchor=CENTER)
    tree1.column("Name",width=100,anchor=CENTER)
    tree1.column("Category",width=100,anchor=CENTER)
    tree1.column("Price",width=100,anchor=CENTER)
    tree1.column("Pages",width=100,anchor=CENTER)
    tree1.heading("ISBN",text="ISBN",anchor=CENTER)
    tree1.heading("Name",text="Name",anchor=CENTER)
    tree1.heading("Category",text="Category",anchor=CENTER)
    tree1.heading("Price",text="Price",anchor=CENTER)
    tree1.heading("Pages",text="Pages",anchor=CENTER)
    tree1['show']='headings'
    tree1.pack()
    s_btn['state'] = 'disabled'
    def delete():
        cat.delete(value)
        clear_all()
    def clear_all():
        tree1.destroy()
        hsb1.destroy()
        s_btn['state'] = 'normal'
    clear_btn = tk.Button(frame3, text='clear',command=clear_all)
    clear_btn.pack(fill='x', ipady=15)
    clear_btn.place(x=600,y=500)
    delete_btn = tk.Button(frame3, text='delete',command=delete)
    delete_btn.pack(fill='x', ipady=15)
    delete_btn.place(x=800,y=500)
    
search=Label(frame3,text='Search ',fg='black',bg='#fff0f5')
search.pack(pady=(20,5))
search.config(font=('veranda',15))
search_input=Entry(frame3,width=50)#text input on screen
search_input.pack(ipady=4,pady=(10,5)) #ipady for height
s_btn = tk.Button(frame3, text='Search',command=search_func)
s_btn.pack(fill='x', ipady=15)
s_btn.place(x=200,y=500)
back_btn = tk.Button(frame3, text='Back',command=lambda:show_frame(frame1))
back_btn.pack(fill='x', ipady=15)
back_btn.place(x=1000,y=500)


#==================Frame 4 code

def insert_func():
    print("hi")
    isbn = isbn_input.get()
    book = book_input.get()
    genre = genre_input.get()
    pgno = pgno_input.get()
    price = price_input.get()
  

    lst=[book,genre,price,pgno]
    print(lst)

    insertion = cat.insert(isbn, lst)
   

    pass

Insert=Label(frame4,text='INSERT',fg='black',bg='#fff0f5')
Insert.pack(pady=(20,5))
Insert.config(font=('veranda',15))

isbn = Label(frame4,text='  ISBN',fg='black',bg='#fff0f5',font=('Times New Roman',20,'bold')).place(x=350,y=58)
isbn_input=Entry(frame4,width=50)#text input on screen
isbn_input.pack(ipady=4,pady=(10,5)) #ipady for height

book = Label(frame4,text='Book Name',fg='black',bg='#fff0f5',font=('Times New Roman',20,'bold')).place(x=330,y=98)
book_input=Entry(frame4,width=50)#text input on screen
book_input.pack(ipady=4,pady=(10,5)) #ipady for height

genre = Label(frame4,text='Genre',fg='black',bg='#fff0f5',font=('Times New Roman',20,'bold')).place(x=350,y=138)
genre_input=Entry(frame4,width=50)#text input on screen
genre_input.pack(ipady=4,pady=(10,5)) #ipady for height

pgno = Label(frame4,text='Page Number',fg='black',bg='#fff0f5',font=('Times New Roman',20,'bold')).place(x=320,y=178)
pgno_input=Entry(frame4,width=50)#text input on screen
pgno_input.pack(ipady=4,pady=(10,5)) #ipady for height

price = Label(frame4,text='Price',fg='black',bg='#fff0f5',font=('Times New Roman',20,'bold')).place(x=350,y=224)
price_input=Entry(frame4,width=50)#text input on screen
price_input.pack(ipady=4,pady=(10,5)) #ipady for height





i_btn = tk.Button(frame4, text='INSERT',font=('Times New Roman',20,'bold'),command=insert_func)
i_btn.pack(ipady=10)
i_btn.place(x=500,y=500)


frame4_btn = tk.Button(frame4, text='Wapsi',command=lambda:show_frame(frame1))
frame4_btn.pack(fill='x', ipady=15)










# name=Label(root,text='Book Name ',fg='black',bg='#fff0f5')
# name.pack(pady=(20,5))
# name.config(font=('veranda',15))
# name_input=Entry(root,width=50)#text input on screen
# name_input.pack(ipady=4,pady=(10,5)) #ipady for height
# category=Label(root,text='Category ',fg='black',bg='#fff0f5')
# category.pack(pady=(20,5))
# category.config(font=('veranda',15))
# cat_input=Entry(root,width=50)#text input on screen
# cat_input.pack(ipady=4,pady=(10,5)) #ipady for height
# price=Label(root,text='Price ',fg='black',bg='#fff0f5')
# price.pack(pady=(20,5))
# price.config(font=('veranda',15))
# price_input=Entry(root,width=50)#text input on screen
# price_input.pack(ipady=4,pady=(10,5)) #ipady for height
# pages=Label(root,text='Pages ',fg='black',bg='#fff0f5')
# pages.pack(pady=(20,5))
# pages.config(font=('veranda',15))
# pages_input=Entry(root,width=50)#text input on screen
# pages_input.pack(ipady=4,pady=(10,5)) #ipady for height
# insert=Button(root,width=20)
# insert.pack(pady=(20,5))
show_frame(frame1)
window.mainloop()
