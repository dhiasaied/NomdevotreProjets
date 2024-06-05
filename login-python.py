from tkinter import *
import os

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x450")  # Increase the height to accommodate new fields

    global username, password, name, email
    global username_entry, password_entry, name_entry, email_entry

    username = StringVar()
    password = StringVar()
    name = StringVar()
    email = StringVar()

    Label(register_screen, text="Inscription",width="300", height="2", bg="red", fg="white").pack()
    Label(register_screen, text="").pack()

    # New fields for name
    name_label = Label(register_screen, text="First Name * ")
    name_label.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()

    username_label = Label(register_screen, text="Last Name * ")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    # New fields for email
    email_label = Label(register_screen, text="Email * ")
    email_label.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    password_label = Label(register_screen, text="Password * ")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    # New field for confirming password
    confirm_password_label = Label(register_screen, text="Confirm Password * ")
    confirm_password_label.pack()
    confirm_password_entry = Entry(register_screen, show='*')
    confirm_password_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Envoyer", width=30, height=1, bg="blue", fg="white", command=register_user).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    name_info = name.get()
    email_info = email.get()
    confirm_password_info = confirm_password_entry.get()

    # Check if passwords match
    if password_info == confirm_password_info:
        file = open(username_info, "w")
        file.write("Name: " + name_info + "\n")
        file.write("Email: " + email_info + "\n")
        file.write("Username: " + username_info + "\n")
        file.write("Password: " + password_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        confirm_password_entry.delete(0, END)

        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    else:
        Label(register_screen, text="Passwords do not match", fg="red").pack()
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    Label(login_screen, text="login",width="300", height="2",bg="red", fg="white").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Envoyer",  width=30, height=1, bg="blue", fg="white", command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x250")
    main_screen.title("Account Login")
    Label(text="Sign-up", bg="blue", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Inscription", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()