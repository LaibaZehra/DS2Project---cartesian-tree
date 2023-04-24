import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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


background2= Canvas(frame2,height = 0, width = 0)
img22 = PhotoImage(file="wallpaper.png")
background_label2 = Label(frame2,image=img22,bg="pink")
background_label2.place(x=0,y=0,relwidth=1, relheight=1)
background2.pack()






#==================Frame 2 code


def view1():
    one_wapsi_button = 0
    def delete():
        global one_wapsi_button
        one_wapsi_button = 1
        tree.destroy()
        hsb.destroy()
        if one_wapsi_button == 1:
            frame2_btn.destroy()
    lst=cat.inorder()
    tree=ttk.Treeview(frame2)
    s=ttk.Style(frame2)
    count=0
    for i in lst:
        tree.insert('',count,text="",values=(i,lst[i][0],lst[i][1],lst[i][2],lst[i][3]))
        count+=1
    frame2_btn = tk.Button(frame2, text='Back',fg='black',bg='sienna1',font=('Times New Roman',25,'bold'),command=lambda:[show_frame(frame1),delete()])
    frame2_btn.place(x=600,y=200)
    frame2_btn.pack()
  
    VIEW=Label(frame2,text='VIEW ALL BOOKS',fg='white',bg='black',font=('Times New Roman',30,'bold')).place(x=150,y=15)
    
    s.theme_use('clam') 
    s.configure(".",font=('Times New Roman',12))
    s.configure("Treeview.Heading",foreground='black',fg='white',bg='black',font=('Times New Roman',15))
    hsb=ttk.Scrollbar(frame2,orient='vertical')
    hsb.configure(command=tree.yview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)
    tree['columns']=("ISBN","Name","Category","Price","Pages")
    tree.configure(height=26)
    tree.column("ISBN",width=100,anchor=CENTER)
    tree.column("Name",width=400,anchor=CENTER)
    tree.column("Category",width=300,anchor=CENTER)
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
img = PhotoImage(file="wallpaper.png")
background_label = Label(frame1,image=img,bg="pink")
background_label.place(x=0,y=0,relwidth=1, relheight=1)
background.pack()

searchimg = PhotoImage(file="search button.png")
Label(frame1,image=searchimg,bg="white").place(x=200,y=200)


viewimg = PhotoImage(file="view button.png")
Label(frame1,image=viewimg,bg="white").place(x=500,y=200)


deleteimg = PhotoImage(file="insert.png")
Label(frame1,image=deleteimg,bg="white").place(x=800,y=200)

Heading=Label(frame1,text='Fries Library Management System',fg='white',bg='black',font=('Times New Roman',40,'bold'))

Heading.pack() #print on the screen
Heading.place(x=250,y=20)


frame1_btn = tk.Button(frame1, text='View',fg="black",bg="sienna",font=('Times New Roman',24,'bold'),command=lambda:[show_frame(frame2),view1()])
frame1_btn.pack(ipady=15)
frame1_btn.place(x=550,y=520)

search_btn = tk.Button(frame1, text='Search/Delete',fg="black",bg="sienna",font=('Times New Roman',24,'bold'),command=lambda:show_frame(frame3))
search_btn.pack(ipady=15)
search_btn.place(x=195,y=520)

insert_btn = tk.Button(frame1, text='Insert',fg="black",bg="sienna",font=('Times New Roman',24,'bold'),command=lambda:show_frame(frame4))
insert_btn.pack(ipady=15)
insert_btn.place(x=850,y=520)


window.title('Fries Management System') # heading of the window
window.iconbitmap('icon.ico') #icon of the window

#==================Frame 2 code



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
    tree1.column("ISBN",width=100,anchor=CENTER)
    tree1.column("Name",width=400,anchor=CENTER)
    tree1.column("Category",width=300,anchor=CENTER)
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
        
        msg_box = tk.messagebox.askquestion('Confirmation', 'Are you sure you want to delete this record?',
                                        icon='warning')
        if msg_box == 'yes':
            cat.delete(value)
            clear_all()
            messagebox.showinfo("Message", "You have deleted a record.")
        # else:
        #     tk.messagebox.showinfo('Return', 'You will now return to the application screen')
    def clear_all():
        tree1.destroy()
        hsb1.destroy()
        s_btn['state'] = 'normal'
    clear_btn = tk.Button(frame3, text='clear',command=clear_all,bg='sienna',font=('Times New Roman',25,'bold'),fg='black')
    clear_btn.pack(fill='x', ipady=15)
    clear_btn.place(x=500,y=450)
    delete_btn = tk.Button(frame3, text='delete',command=delete,bg='sienna',font=('Times New Roman',25,'bold'),fg='black')
    delete_btn.pack(fill='x', ipady=15)
    delete_btn.place(x=700,y=450)

bd = Canvas(frame3,height = 10, width = 10)
img2 = PhotoImage(file="wallpaper.png")
background_label2 = Label(frame3,image=img2,bg="pink")
background_label2.place(x=0,y=0,relwidth=1, relheight=1)
bd.pack()
    
search=Label(frame3,text='Search',fg='white',bg='black',font=('Times New Roman',40,'bold'))
search.pack(pady=(20,5))

search_input=Entry(frame3,width=50)#text input on screen
search_input.pack(ipady=10,pady=(10,5)) #ipady for height


s_btn = tk.Button(frame3, text='Search',command=search_func,bg='sienna1',font=('Times New Roman',22,'bold'),fg='black')
s_btn.pack(fill='x', ipady=15)
s_btn.place(x=200,y=500)
back_btn = tk.Button(frame3, text='Back',command=lambda:show_frame(frame1),bg='sienna1',font=('Times New Roman',22,'bold'),fg='black')
back_btn.pack(fill='x', ipady=15)
back_btn.place(x=1000,y=500)


#==================Frame 4 code
frame4_btn = tk.Button(frame4, text='Wapsi',command=lambda:show_frame(frame1))
frame4_btn.pack(fill='x', ipady=15)
bg = Canvas(frame4,height = 200, width = 200)
img3 = PhotoImage(file="wallpaper.png")
background_label2 = Label(frame4,image=img3,bg="pink")
background_label2.place(x=0,y=0,relwidth=1, relheight=1)
bg.pack()

def insert_func():
    isbn = isbn_input.get()
    book = book_input.get()
    genre = genre_input.get()
    pgno = pgno_input.get()
    price = price_input.get()
    
   
    
   
    # if (isbn==""):
    #    val=messagebox.showinfo("Message", "Please enter the ISBN.")
    # if (book==""):
        
    #     val1=messagebox.showinfo("Message", "Please enter the book name.")
    # if (genre==""):
        
    #     val2=messagebox.showinfo("Message", "Please enter the genre.")
    # if (pgno==""):
       
    #     val3=messagebox.showinfo("Message", "Please enter the page number.")
    # if (price==""):
    #     val4=messagebox.showinfo("Message", "Please enter the price.")
    # i_btn['state'] = 'disabled'
    
    if (isbn=="" or book=="" or genre=="" or pgno=="" or price==""):
       i_btn['state'] = 'normal'
       insert_func()
    else:
        ans=cat.search(isbn)
        if ans==None:
            lst=[book,genre,price,pgno]
            cat.insert(isbn, lst)
            messagebox.showinfo("Message", "You have added a record.")
        else:
           messagebox.showinfo("Message", "The book has already been added.") 




Insert=Label(frame4,text='INSERT BOOKS',fg='white',bg='black',font=('Times New Roman',40,'bold')).place(x=400,y=100)


isbn = Label(frame4,text='ISBN:',fg='white',bg='black',font=('Times New Roman',25,'bold')).place(x=200,y=260)
isbn_input=Entry(frame4,width=50)#text input on screen
isbn_input.pack(ipady=10,pady=(10,5)) #ipady for height

book = Label(frame4,text='Book Name:',fg='white',bg='black',font=('Times New Roman',25,'bold')).place(x=200,y=320)
book_input=Entry(frame4,width=50)#text input on screen
book_input.pack(ipady=10,pady=(10,10))#ipady for height

genre = Label(frame4,text='Genre:',fg='white',bg='black',font=('Times New Roman',25,'bold')).place(x=200,y=380)
genre_input=Entry(frame4,width=50)#text input on screen
genre_input.pack(ipady=10,pady=(10,5)) #ipady for height

pgno = Label(frame4,text='Page Number:',fg='white',bg='black',font=('Times New Roman',25,'bold')).place(x=200,y=440)
pgno_input=Entry(frame4,width=50)#text input on screen
pgno_input.pack(ipady=10,pady=(10,5)) #ipady for height

price = Label(frame4,text='Price:',fg='white',bg='black',font=('Times New Roman',25,'bold')).place(x=200,y=500)
price_input=Entry(frame4,width=50)#text input on screen
price_input.pack(ipady=10,pady=(10,5)) #ipady for height




i_btn = tk.Button(frame4, text='INSERT',fg='black',bg='sienna1',font=('Times New Roman',20,'bold'),command=insert_func)
i_btn.pack(ipady=10)
i_btn.place(x=550,y=550)
def empty():
    print("in")
    isbn_input.delete(0,END)
    book_input.delete(0,END)
    genre_input.delete(0,END)
    pgno_input.delete(0,END)
    price_input.delete(0,END)
b_btn = tk.Button(frame4, text='Back',fg='black',bg='sienna',font=('Times New Roman',30,'bold'),command=lambda:[show_frame(frame1),empty()])
b_btn.pack(ipady=10)
b_btn.place(x=1090,y=550)













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
