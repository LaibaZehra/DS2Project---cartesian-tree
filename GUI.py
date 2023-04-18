from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Fries Management System') # heading of the window
root.iconbitmap('icon.ico') #icon of the window
root.minsize(1000,1000) # minimum size of the window
root.geometry('500x500') # size of the window
root.configure(background='#fff0f5') # bg of screen
image=Image.open('icon.png') # reading the image
resized=image.resize((50,50)) # resizing it
img=ImageTk.PhotoImage(resized) #reading the file
image_label=Label(root,image=img) #making a label to print on the screen
image_label.pack(pady=(10,10)) #move the picture uo and down
text=Label(root,text='Fries Library Management System',fg='black',bg='#fff0f5')
text.pack() #print on the screen
text.config(font=('verdana',24))
isbn=Label(root,text='ISBN ',fg='black',bg='#fff0f5')
isbn.pack(pady=(20,5))
isbn.config(font=('veranda',15))
isbn_input=Entry(root,width=50)#text input on screen
isbn_input.pack(ipady=4,pady=(10,5)) #ipady for height
name=Label(root,text='Book Name ',fg='black',bg='#fff0f5')
name.pack(pady=(20,5))
name.config(font=('veranda',15))
name_input=Entry(root,width=50)#text input on screen
name_input.pack(ipady=4,pady=(10,5)) #ipady for height
category=Label(root,text='Category ',fg='black',bg='#fff0f5')
category.pack(pady=(20,5))
category.config(font=('veranda',15))
cat_input=Entry(root,width=50)#text input on screen
cat_input.pack(ipady=4,pady=(10,5)) #ipady for height
price=Label(root,text='Price ',fg='black',bg='#fff0f5')
price.pack(pady=(20,5))
price.config(font=('veranda',15))
price_input=Entry(root,width=50)#text input on screen
price_input.pack(ipady=4,pady=(10,5)) #ipady for height
pages=Label(root,text='Pages ',fg='black',bg='#fff0f5')
pages.pack(pady=(20,5))
pages.config(font=('veranda',15))
pages_input=Entry(root,width=50)#text input on screen
pages_input.pack(ipady=4,pady=(10,5)) #ipady for height
insert=Button(root,width=20)
insert.pack(pady=(20,5))
root.mainloop()
