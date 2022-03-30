from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

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
    '''saves information to json file'''
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email": email,
            "password": password
        }
    }

    # Checks if the entry boxes are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    
    else:
        # At start we won't have any json file. Hence, including exception handling
        try:
            with open('passwords.json',mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open('passwords.json', mode='w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent= 4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open('passwords.json',mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent= 4)
                
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    '''searches for the password of the website you entered.'''
    website = website_entry.get()

    # Exception handling if file doesn't exists 
    try:
        with open('passwords.json') as data_file:
            data = json.load(data_file)
    
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title= website, message= f"Email: {email}\nPassword: {password}")
        
        else:
            messagebox.showinfo(title="Error",message=f"Details for {website} does not exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")

# Setting up canvas
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

# Textboxes
website_entry = Entry(width=33,bg="white")
website_entry.grid(column=1,row=1)
website_entry.focus()

email_entry = Entry(width=52,bg="white")
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "example@gmail.com" )

password_entry = Entry(width=33,bg="white")
password_entry.grid(column=1,row=3)

# Buttons
generate_button = Button(text="Generate Password",bg="white",command=password_generator)
generate_button.grid(column=2,row=3)

add_button = Button(text= "Add",width=44,bg="white",highlightthickness=0,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text = "Search",bg="white",width=14,command=find_password)
search_button.grid(column=2,row=1)

window.mainloop()