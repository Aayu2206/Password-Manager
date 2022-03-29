from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    '''generates a new password'''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]

    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_numbers =[choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    
    # inserts password in the entry box
    password_entry.insert(0, password)

    # copies password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    '''saves information to txt file'''
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Check your details: \nEmail: {email}\nWebsite: {website}"
                                                        f"\nPassword: {password}\nIs it ok to save?")
    
        if is_ok:
            with open('passwords.txt',mode='a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)   
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")


canvas = Canvas(width= 200,height= 200,bg="white",highlightthickness=0)
logo = PhotoImage(file= 'logo.png')
canvas.create_image(100,112,image= logo)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text="Website:",bg="white")
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:",bg="white")
username_label.grid(column=0,row=2)

password_label = Label(text="Password:",bg="white")
password_label.grid(column=0,row=3)

# Buttons
generate_button = Button(text="Generate Password",bg="white",command=password_generator)
generate_button.grid(column=2,row=3)

add_button = Button(text= "Add",width=44,bg="white",highlightthickness=0,command=save)
add_button.grid(column=1,row=4,columnspan=2)

# Textboxes
website_entry = Entry(width=52,bg="white")
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=52,bg="white")
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "example@gmail.com" )

password_entry = Entry(width=33,bg="white")
password_entry.grid(column=1,row=3)


window.mainloop()