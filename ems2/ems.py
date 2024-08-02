from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
from database import *

#Mode set
set_appearance_mode("dark")

#connect to MySQL
connection, cursor = connect_to_mysql()

#Create main window
window = CTk()
window.geometry('1024x768')
window.resizable(0,0)
window.title('Employee Management System')

#Function to show specific page
def show_page(page_index):
    # Hide all pages
    for index, page in enumerate(pages):
        page.place_forget()
        buttons[index].configure(font=("Helvetica", 14, "normal"))

    # Show the selected page
    pages[page_index].place(x=0, y=40, width=1024, height=768)
    buttons[page_index].configure(font=("Helvetica", 14, "bold"))


# Create pages
page1 = Frame(window, bg="#0C0D2A")
page2 = Frame(window, bg="#0C0D2A")

# Top bar buttons
button_frame = Frame(window, bg="#181a49")
button_frame.place(x=0, y=0, width=1024, height=40)
button1 = CTkButton(button_frame,
                 text="Add Employee",
                 command=lambda: show_page(0),
                 fg_color='#181a49', 
                 hover_color='#252974', 
                 bg_color='#181a49')
button1.pack(side=LEFT, padx=(15, 0), pady=6)
button2 = CTkButton(button_frame,
                 text="Employee List",
                 command=lambda: show_page(1),
                 fg_color='#181a49', 
                 hover_color='#252974', 
                 bg_color='#181a49')
button2.pack(side=LEFT, pady=6)

pages = [page1, page2]
buttons = [button1, button2]

# Initially show the first page
show_page(1)

#inputs
employee_id_var = StringVar()
full_name_var = StringVar()
gender_var = StringVar()
email_id_var = StringVar()
contact_number_var = StringVar()
date_of_joining_var = StringVar()
department_var = StringVar()
address_var = StringVar()

# Function to add an employee
def add_employee():
    if (employee_id_var.get() == ""
            or full_name_var.get() == ""
            or gender_var.get() == ""
            or email_id_var.get() == ""
            or contact_number_var.get() == ""
            or date_of_joining_var.get() == ""
            or department_var.get() == ""
            or address_entry.get("1.0", "end") == ""):

        messagebox.showerror("Input Error", "Please fill in all details")
        return

    # Insert data into the database
    data_to_insert = (employee_id_var.get(),
                      full_name_var.get(),
                      gender_var.get(),
                      email_id_var.get(),
                      contact_number_var.get(),
                      date_of_joining_var.get(),
                      department_var.get(),
                      address_entry.get("1.0", "end"))
    insert_data(connection, cursor, data_to_insert)
    messagebox.showinfo("Success", "Record Inserted")
    clear_all()
    display_all_records()

# Function to clear all input fields
def clear_all():
    employee_id_var.set("")
    full_name_var.set("")
    gender_var.set("")
    email_id_var.set("")
    contact_number_var.set("")
    date_of_joining_var.set("")
    department_var.set("")
    address_entry.delete("1.0", "end")


# Define selected_row at the beginning of your script
selected_row = None
# Function to get data from the selected row in the Treeview
def get_selected_row(event):
    global selected_row
    selected_row = table.focus()  # Focus on the selected table row
    data = table.item(selected_row)  # Get the data from the selected row
    global selected_data
    selected_data = data["values"]  # Store the data in another variable

    # Set the values in the input fields
    employee_id_var.set(selected_data[0])
    full_name_var.set(selected_data[1])
    gender_var.set(selected_data[2])
    email_id_var.set(selected_data[3])
    contact_number_var.set(selected_data[4])
    date_of_joining_var.set(selected_data[5])
    department_var.set(selected_data[6])
    address_entry.delete("1.0", "end")
    address_entry.insert(END, selected_data[7])


# Function to display all records in the Treeview
def display_all_records():
    table.delete(*table.get_children())
    for selected_data in fetch_data(cursor):
        table.insert("", END, values=selected_data)


# Function to show the update page
def show_update_page():
    if not selected_row:
        messagebox.showinfo("Info", "Please select data from the table.")
        return

    # Hide page2
    page2.place_forget()
    button2.configure(font=("Helvetica", 12, "normal"))
    submit_button.destroy()
    clear_button.destroy()

    # Show page1
    show_page(0)
    global update_submit_button, cancel_button
    update_submit_button = CTkButton(master=page1,
                                     command=update_employee,
                                     text="Update",
                                     font=("Helvetica", 16, "bold"),
                                     text_color="white",
                                     width=105,
                                     height=35,
                                     corner_radius=6,
                                     fg_color="#359f07",
                                     hover_color="#2e7e0c")
    update_submit_button.place(x=805, y=630)
    cancel_button = CTkButton(master=page1,
                              command=cancel_update,
                              text="Cancel",
                              font=("Helvetica", 16, "bold"),
                              text_color="white",
                              width=105,
                              height=35,
                              corner_radius=6)
    cancel_button.place(x=670, y=630)

# Function to update an employee record
def update_employee():
    if (employee_id_var.get() == ""
            or full_name_var.get() == ""
            or gender_var.get() == ""
            or email_id_var.get() == ""
            or contact_number_var.get() == ""
            or date_of_joining_var.get() == ""
            or department_var.get() == ""
            or address_entry.get("1.0", "end") == ""):

        messagebox.showerror("Input Error", "Please fill in all details")
        return

    # Update data in the database
    data_to_insert = (employee_id_var.get(),
                      full_name_var.get(),
                      gender_var.get(),
                      email_id_var.get(),
                      contact_number_var.get(),
                      date_of_joining_var.get(),
                      department_var.get(),
                      address_entry.get("1.0", "end"))

    update_data(connection, cursor, data_to_insert, selected_data[0])
    messagebox.showinfo("Success", "Record updated")
    clear_all()
    display_all_records()
    show_page(1)
    global selected_row
    selected_row = None
    
    update_submit_button.destroy()
    cancel_button.destroy()

    clear_button = CTkButton(master=page1,
                             command=clear_all,
                             text="Clear",
                             font=("Helvetica", 18),
                             text_color="white",
                             width=120,
                             height=40,
                             corner_radius=6)
    clear_button.place(x=1020, y=650)
    submit_button = CTkButton(master=page1,
                              command=add_employee,
                              text="Submit",
                              font=("Helvetica", 18),
                              text_color="white",
                              width=120,
                              height=40,
                              corner_radius=6,
                              fg_color="#359f07",
                              hover_color="#2e7e0c")
    submit_button.place(x=1160, y=650)


# Function to cancel the update and go back to the main page
def cancel_update():
    update_submit_button.destroy()
    cancel_button.destroy()

    clear_button = CTkButton(master=page1,
                             command=clear_all,
                             text="Clear",
                             font=("Helvetica", 18),
                             text_color="white",
                             width=120,
                             height=40,
                             corner_radius=6)
    clear_button.place(x=1020, y=650)
    submit_button = CTkButton(master=page1,
                              command=add_employee,
                              text="Submit",
                              font=("Helvetica", 18),
                              text_color="white",
                              width=120,
                              height=40,
                              corner_radius=6,
                              fg_color="#359f07",
                              hover_color="#2e7e0c")
    submit_button.place(x=1160, y=650)
    clear_all()
    display_all_records()
    show_page(1)
    global selected_row
    selected_row = None

# Function to delete all records
def delete_all_records():
    if not selected_row:
        messagebox.showinfo("Info", "Please select data from the table.")
        return
    remove_data(connection, cursor, selected_data[0])
    clear_all()
    display_all_records()


# page1 contents
# system title
main_label = CTkLabel(page1,
                   text="Employee management system",
                   font=("Helvetica", 20, "bold"),
                   text_color="#FFFFFF",
                   bg_color="#0C0D2A")
main_label.place(relx=0.5, y=25, anchor=CENTER)
container = CTkEntry(master=page1,
                bg_color="#0C0D2A",
                fg_color="#0a0b1f",
                corner_radius=12,
                width=900,
                height=650)
container.place(relx=0.5, rely=0.49, anchor=CENTER)
container.configure(state="disabled")

# Employee_ID Input fields
employee_id_label = Label(page1,
                          text="Employee ID",
                          font=("Helvetica", 14),
                          fg="white",
                          bg="#0a0b1f")
employee_id_label.place(x=120, y=100)

employee_id_entry = CTkEntry(master=page1,
                             textvariable=employee_id_var,
                             font=("Helvetica", 14),
                             width=360,
                             height=35,
                             fg_color=("", "#1d1f32"),
                             corner_radius=6)
employee_id_entry.place(x=120, y=140)

# Name Input fields
name_label = Label(page1,
                   text="Name",
                   font=("Helvetica", 14),
                   fg="white",
                   bg="#0a0b1f")
name_label.place(x=550, y=100)
name_entry = CTkEntry(master=page1,
                      textvariable=full_name_var,
                      font=("Helvetica", 14),
                      width=360,
                      height=35,
                      fg_color=("", "#1d1f32"),
                      corner_radius=6)
name_entry.place(x=550, y=140)

# Gender Input fields
gender_label = Label(page1,
                     text="Gender",
                     font=("Helvetica", 14),
                     fg="white",
                     bg="#0a0b1f")
gender_label.place(x=550, y=220)
genders = ["Male", "Female"]
gender_entry = CTkComboBox(master=page1,
                           variable=gender_var,
                           width=360,
                           height=30,
                           font=("Helvetica", 14),
                           dropdown_font=("Helvetica", 14),
                           dropdown_fg_color="#1d1f32",
                           dropdown_text_color="white",
                           dropdown_hover_color="#0a0b1f",
                           fg_color=("", "#1d1f32"),
                           corner_radius=6,
                           state="readonly",
                           values=genders)
gender_entry.place(x=550, y=260)

#Email Input fields
email_label = Label(page1,
                    text="Email ID",
                    font=("Helvetica", 14),
                    fg="white",
                    bg="#0a0b1f")
email_label.place(x=120, y=220)
email_entry = CTkEntry(master=page1,
                       textvariable=email_id_var,
                       font=("Helvetica", 14),
                       width=360,
                       height=30,
                       fg_color=("", "#1d1f32"),
                       corner_radius=6)
email_entry.place(x=120, y=260)

#Contact Input fields
contact_label = Label(page1,
                      text="Contact Number",
                      font=("Helvetica", 14),
                      fg="white",
                      bg="#0a0b1f")
contact_label.place(x=120, y=340)
contact_entry = CTkEntry(master=page1,
                         textvariable=contact_number_var,
                         font=("Helvetica", 14),
                         width=360,
                         height=30,
                         fg_color=("", "#1d1f32"),
                         corner_radius=6)
contact_entry.place(x=120, y=380)

#Date of Joining Input fields
doj_label = Label(page1,
                  text="Date of Joining",
                  font=("Helvetica", 14),
                  fg="white",
                  bg="#0a0b1f")
doj_label.place(x=550, y=340)
doj_entry = CTkEntry(master=page1,
                     textvariable=date_of_joining_var,
                     font=("Helvetica", 14),
                     placeholder_text="dd/mm/yy",
                     width=360,
                     height=30,
                     fg_color=("", "#1d1f32"),
                     corner_radius=6)
doj_entry.place(x=550, y=380)

# Department Input fields
department_label = Label(page1,
                         text="Department",
                         font=("Helvetica", 14),
                         fg="white",
                         bg="#0a0b1f")
department_label.place(x=120, y=460)
departments = ["Research and Development (R&D)", "Scientific Operations",
               "Software Engineering", "Data Science and Analytics", 
               "Computational Biology", "Machine Learning",
               "Quality Assurance (QA)", "Product Management", 
               "Business & Finance", "Marketing and Partnership"]
department_entry = CTkComboBox(master=page1,
                               variable=department_var,
                               width=360,
                               height=30,
                               font=("Helvetica", 14),
                               dropdown_font=("Helvetica", 14),
                               dropdown_fg_color="#1d1f32",
                               dropdown_text_color="white",
                               dropdown_hover_color="#0a0b1f",
                               fg_color=("", "#1d1f32"),
                               corner_radius=6,
                               values=departments,
                               state="readonly")
department_entry.place(x=120, y=500)

# Address_inputfields
address_label = Label(page1,
                      text="Address",
                      font=("Helvetica", 14),
                      fg="white",
                      bg="#0a0b1f")
address_label.place(x=550, y=460)
address_entry = CTkTextbox(master=page1,
                           font=("Helvetica", 14),
                           width=360,
                           height=90,
                           fg_color=("", "#1d1f32"),
                           corner_radius=6,
                           border_width=2)
address_entry.place(x=550, y=500)

# Buttons
clear_button = CTkButton(master=page1,
                         command=clear_all,
                         text="Clear",
                         font=("Helvetica", 16, "bold"),
                         text_color="white",
                         width=105,
                         height=35,
                         corner_radius=6)
clear_button.place(x=670, y=630)
submit_button = CTkButton(master=page1,
                          command=add_employee,
                          text="Submit",
                          font=("Helvetica", 16, "bold"),
                          text_color="white",
                          width=105,
                          height=35,
                          corner_radius=6,
                          fg_color="#359f07",
                          hover_color="#2e7e0c")
submit_button.place(x=805, y=630)

# page2 contents display employee list page
# system title
main_label = Label(page2,
                   text="Employee Management System",
                   font=("Helvetica", 16, "bold"),
                   fg="white",
                   bg="#0C0D2A")
main_label.place(relx=0.5, y=25, anchor=CENTER)

# Treeview configuration
tree_frame = Frame(page2,
                   bg="#0C0D2A")
tree_frame.place(x=12, y=50, width=1000, height=650)

style = ttk.Style()
style.theme_use('clam')

style.configure("mystyle.Treeview",
                background="#0a0b1f", 
                fieldbackground="#0a0b1f", 
                foreground="white",
                font=("Helvetica", 10),
                rowheight=30)
style.configure("mystyle.Treeview.Heading",
                background="#181a49",
                fieldbackground="#181a49", 
                foreground="white",
                font=("Helvetica", 12), 
                rowheight=50)
style.map('Treeview',
	background=[('selected', "#1d2559")])

style.map("mystyle.Treeview.Heading",
          background=[('active', '#252974')],
          foreground=[('active', 'white')])

style.layout("mystyle.Treeview",
             [('Treeview.field', {'sticky': 'nswe', 'border': '1'})])

table = ttk.Treeview(tree_frame,
                     column=(1, 2, 3, 4, 5, 6, 7, 8),
                     show="headings",
                     style="mystyle.Treeview")
table.column("1", width=100)
table.column("2", width=127)
table.column("3", width=70)
table.column("4", width=140)
table.column("5", width=125)
table.column("6", width=110)
table.column("7", width=110)
table.column("8", width=120)
table.heading("1", text="Employee ID", anchor='center')
table.heading("2", text="Full Name", anchor='center')
table.heading("3", text="Gender", anchor='center')
table.heading("4", text="Email", anchor='center')
table.heading("5", text="Contact Number", anchor='center')
table.heading("6", text="Date of Joining", anchor='center')
table.heading("7", text="Department", anchor='center')
table.heading("8", text="Address", anchor='center')
table.bind("<ButtonRelease-1>", get_selected_row)
table.place(x=0, y=0, width=1000, height=570)

scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scroll.set)
scroll.place(x=1020, y=80, height=568)

# Buttons for page 2
update_button = CTkButton(master=page2,
                          command=show_update_page,
                          text="Update",
                          font=("Helvetica", 18),
                          text_color="white",
                          width=105,
                          height=35,
                          corner_radius=6)
update_button.place(x=700, y=650)
delete_button = CTkButton(master=page2,
                          command=delete_all_records,
                          text="Delete",
                          font=("Helvetica", 18),
                          text_color="white",
                          width=105,
                          height=35,
                          corner_radius=6,
                          fg_color="#ca3e30",
                          hover_color="#ba1b0a")
delete_button.place(x=850, y=650)

# Display employee data in the Treeview
for row in fetch_data(cursor):
    table.insert("", END, values=row)

# Run the main loop
window.mainloop()