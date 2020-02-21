#import modules

from tkinter import *
import os
import aswin
"""This is the main gui of the register form i have made"""
# Designing window for registration
class registerscreenz:
    def register(self):
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("500x450")
        

        global username
        global password
        global username_entry
        global password_entry
        global error #error shows error message
        username = StringVar()
        password = StringVar()

        Label(register_screen, text="Please enter details below",).pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1 , command = register_user).pack()
        error = StringVar()  #error 
        Label(register_screen, textvariable=error).pack() #label to show password validation


# Designing window for login
"""This is the main gui of the login form i have made"""
class loginscreenz:
    def login(self):
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
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
        Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    '''This is where i have implemented what will nhappen after i click on the register button'''
    # Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()
    if (len(password_info)<9): #if length of password is less than 9
        error.set("Password length must be greater than 9")
        return None #return none
    else:
        digit=0 #flags to check validation
        upper=0
        lower=0
        for i in password_info: #iterates through each letter in password
            if (i.isdigit()): #if the letter is number
                digit=1
            if (i.isupper()): #if the letter is upper case
                upper=1
            if (i.islower()): #if the letter is lower case
                lower=1
        if (digit==0): #if there is no digit in password
            error.set("Password must contain atleast one digit")
            return None
        if (upper==0): #if there is no uppercase letter in password
            error.set("Password must contain atleast one uppercase letter")
            return None
        if (lower==0): #if there is no lowercase letter in password
            error.set("Password must contain atleast one lowercase letter")
            return None
    error.set("")

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Account Creation Success", fg="green", font=("calibri", 11)).pack()
'''This is where i have implemented what will nhappen after i click on the login button'''
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
            login_success()
            

        else:
            password_not_recognised()

    else:
        user_not_found()
        

'''This is where i have done error handeling where if ther is invalid password it show invalid password'''

def login_success():
    global Screen 
    main_screen.withdraw()
    login_screen.withdraw()
    Screen=Toplevel(main_screen)
    aswin.employee_gui(Screen)
'''This is where i have done error handeling where if ther is invalid password it show invalid password'''
# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
'''This is where i have done error handeling where if there is no user found it shows user not found'''
# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
'''This where i destory all the before windows'''
# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

"""This is the main gui of the window i have made"""
# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("800x200")
    main_screen.title("Softwarica Login")
    Label(text="Employee Management System",width="300", fg="blue" , height="2", font=("Calibri", 22)).pack()
    Button(text="Login", height="2", width="30", command = lambda : loginscreenz.login(main_screen)).pack(padx=5, side='left')   #adding padx and pady to arrange horizontally
    Button(text="Create Account", height="2", width="30", command=lambda : registerscreenz.register(main_screen)).pack(padx=5, side='left')
    Button(text="Exit", height="2", width="30",command=main_screen.destroy).pack(padx=5, side='left')
      
    main_screen.mainloop()

if __name__=='__main__':
    

    main_account_screen()