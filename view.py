from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
#root.minsize(1000,1000) # minimum size of the window
root.geometry('500x500') # size of the window
root.configure(background='#fff0f5') # bg of screen
lst=[[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10]]
tree=ttk.Treeview(root)
s=ttk.Style(root)
count=0
for i in lst:
    tree.insert('',count,text="",values=(i[0],i[1],i[2],i[3],i[4]))
    count+=1
s.theme_use('clam')
s.configure(".",font=('Helvetice',11))
s.configure("Treeview.Heading",foreground='blue',font=('Helvetice',15))
hsb=ttk.Scrollbar(root,orient='vertical')
hsb.configure(command=tree.yview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=Y,side=RIGHT)
tree['columns']=("ISBN","Name","Category","Price","Pages")
tree.column("ISBN",width=100,anchor=CENTER)
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
root.mainloop()