from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import messagebox

set_appearance_mode("dark")

def login():
    if user_entry.get()=='' or user_pass.get()=='':
        messagebox.showerror('Error', 'All fields are required to be filled')
    elif user_entry.get()=='afif' and user_pass.get()=='0258789':
        messagebox.showinfo('Success', 'Login is successful')
        window.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong credentials')

window = CTk()
window.geometry('1024x768')
window.resizable(0,0)
window.title('Login Page')
img = CTkImage(Image.open(r'F:\AFIF\PROJECTS\Project\Employee_Management_System_Python_Tkinter_MySQL\img\Screenshot 2024-07-12 050538.png'), 
               size=(1024,768))
image_label = CTkLabel(window, 
                       image=img, 
                       text='')
image_label.place(x=0, y=0)

heading_label = CTkLabel(window, 
                         text='Employee Management System', 
                         text_color='#e2e3f6', 
                         bg_color='#0C0D2A', 
                         font=('Helvetica', 30, 'bold'))
heading_label.place(relx=0.5, y=230, anchor=CENTER)

user_entry = CTkEntry(window, 
                      width=200,
                      placeholder_text='Enter Username', 
                      fg_color=("", '#0a0b1f'))
user_entry.place(relx=0.5, y=290, anchor=CENTER)

user_pass = CTkEntry(window, 
                     width=200,
                     placeholder_text='Enter Password', 
                     fg_color=("", '#0a0b1f'), 
                     show='*')
user_pass.place(relx=0.5, y=350, anchor=CENTER)

login_button = CTkButton(window, 
                         width=100, 
                         text='Login', 
                         fg_color='#1a2caa', 
                         hover_color='#101b68', 
                         bg_color='#0C0D2A', 
                         cursor='hand2',
                         command = login)
login_button.place(relx=0.5, y=410, anchor=CENTER)

window.mainloop()