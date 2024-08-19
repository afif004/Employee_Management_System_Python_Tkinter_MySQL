from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import messagebox

set_appearance_mode("dark")

def login():
    if user_entry.get()=='' or user_pass.get()=='':
        messagebox.showerror('Error', 'All fields are required to be filled')
    elif user_entry.get()=='afif' and user_pass.get()=='0258789':
        messagebox.showinfo('Success', 'Entry is successful')
        window.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong credentials')

window = CTk()
window.geometry('1024x632')
window.resizable(0,0)
window.title('Login Page')
img = CTkImage(Image.open("Employee_Management_System_Python_Tkinter_MySQL\img\Screenshot 2024-07-12 050538.png"), 
               size=(1024,632))
image_label = CTkLabel(window, 
                       image=img, 
                       text='')
image_label.place(x=0, y=0)

heading_label = CTkLabel(window, 
                         text='Employee Management System', 
                         text_color='#e2e3f6', 
                         bg_color='#0C0D2A', 
                         font=('Helvetica', 32, 'bold'))
heading_label.place(relx=0.5, rely=0.32, anchor=CENTER)

user_entry = CTkEntry(window, 
                      height=29,
                      width=278,
                      placeholder_text='Enter Username', 
                      fg_color=("", '#0a0b1f'),
                      font=('Helvetica', 18, 'normal'))
user_entry.place(relx=0.5, rely=0.44, anchor=CENTER)

user_pass = CTkEntry(window, 
                     height=29,
                     width=278,
                     placeholder_text='Enter Password', 
                     fg_color=("", '#0a0b1f'), 
                     show='*',
                     font=('Helvetica', 18, 'normal'))
user_pass.place(relx=0.5, rely=0.56, anchor=CENTER)

login_button = CTkButton(window, 
                         height=40,
                         width=106, 
                         text='Enter', 
                         fg_color='#1a2caa', 
                         hover_color='#101b68', 
                         bg_color='#0C0D2A', 
                         cursor='hand2',
                         command = login,
                         font=('Helvetica', 20, 'bold'))
login_button.place(relx=0.5, rely=0.68, anchor=CENTER)

window.mainloop()