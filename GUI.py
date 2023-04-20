from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

def show_frame(frame):
    frame.tkraise()
    

window= tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


frame1 = tk.Frame(window)



frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

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


frame1_btn = tk.Button(frame1, text='Dosra Form',fg="black",bg="PaleTurquoise",font=('Times New Roman',24,'bold'),command=lambda:show_frame(frame2))
frame1_btn.pack(ipady=15)
frame1_btn.place(x=600,y=300)





#==================Frame 2 code
frame2_title=  tk.Label(frame2, text='Page 2', font='times 35', bg='yellow')
frame2_title.pack(fill='both', expand=True)

frame2_btn = tk.Button(frame2, text='Wapsi',command=lambda:show_frame(frame1))
frame2_btn.pack(fill='x', ipady=15)




window.title('Fries Management System') # heading of the window
window.iconbitmap('icon.ico') #icon of the window





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
