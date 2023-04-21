
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from database import Table
from Cartesiantree import CartesianTree
from Cartesiantree import Node

def show_frame(frame):
    frame.tkraise()
    

window= tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


frame1 = tk.Frame(window)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window) # search and delete


for frame in (frame1, frame2, frame3):
    frame.grid(row=0,column=0,sticky='nsew')
    
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


frame1_btn = tk.Button(frame1, text='View',fg="black",bg="PaleTurquoise",font=('Times New Roman',24,'bold'),command=lambda:show_frame(frame2))
frame1_btn.pack(ipady=15)
frame1_btn.place(x=600,y=300)
search_btn = tk.Button(frame1, text='Search',fg="black",bg="PaleTurquoise",font=('Times New Roman',24,'bold'),command=lambda:show_frame(frame3))
search_btn.pack(ipady=15)
search_btn.place(x=600,y=600)





#==================Frame 2 code
data=Table()
value=data.read('data/books.csv','serial')
cat=CartesianTree(data.keys,0,len(data.keys)-1,data.records)
lst=cat.inorder()
tree=ttk.Treeview(frame2)
s=ttk.Style(frame2)
count=0
for i in lst:
    tree.insert('',count,text="",values=(i,value[i][0],value[i][1],value[i][2],value[i][3]))
    count+=1
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

frame2_btn = tk.Button(frame2, text='Wapsi',command=lambda:show_frame(frame1))
frame2_btn.pack(fill='x', ipady=15)

frame2_btn = tk.Button(frame2, text='Wapsi',command=lambda:show_frame(frame1))
frame2_btn.pack(fill='x', ipady=15)




window.title('Fries Management System') # heading of the window
window.iconbitmap('icon.ico') #icon of the window

#==================Frame 3 code
def search_func():
    value=search_input.get()
    ans=cat.search(value)
    tree1=ttk.Treeview(frame3)
    s1=ttk.Style(frame3)
    count=0
    tree1.insert('',count,text="",values=(value,ans[0],ans[1],ans[2],ans[3]))
    s1.theme_use('clam')
    s1.configure(".",font=('Helvetice',11))
    s1.configure("Treeview.Heading",foreground='black',font=('Times New Roman',15))
    hsb1=ttk.Scrollbar(frame2,orient='vertical')
    hsb1.configure(command=tree.yview)
    tree1.configure(xscrollcommand=hsb.set)
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
    def clear_all():
        for item in tree1.get_children():
            tree1.destroy()
        s_btn['state'] = 'normal'
        tree1.delete()
    clear_btn = tk.Button(frame3, text='clear',command=clear_all)
    clear_btn.pack(fill='x', ipady=15)
    clear_btn.place(x=600,y=500)
    
search=Label(frame3,text='Search ',fg='black',bg='#fff0f5')
search.pack(pady=(20,5))
search.config(font=('veranda',15))
search_input=Entry(frame3,width=50)#text input on screen
search_input.pack(ipady=4,pady=(10,5)) #ipady for height
s_btn = tk.Button(frame3, text='Search',command=search_func)
s_btn.pack(fill='x', ipady=15)
s_btn.place(x=200,y=500)








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
