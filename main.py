from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


FONT = ('calibri', 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    generated_password = "".join(password_list)
    password_entry.insert(END, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = site.get()
    email = name.get()
    given_password = password_entry.get()
    data_dict = {
        website_entry:
                {
                 "email": email,
                 "password": given_password
                }}
    if len(website_entry) == 0 or len(given_password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any of the fields empty!")
    else:
        with open('data.json', 'r') as data:
            # Reading old data
            new_data = json.load(data)
            # Updating old data
            new_data.update(data_dict)
        with open('data.json', 'w') as data:
            # Saving updated data
            json.dump(new_data, data, indent=4)
            site.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

# Labels
website = Label(text='Website:', font=FONT)
website.grid(row=1, column=0)
username = Label(text="Email/Username:", font=FONT)
username.grid(row=2, column=0)
password = Label(text='Password:', font=FONT)
password.grid(row=3, column=0)

# Entries
site = Entry(width=42)
site.grid(row=1, column=1, columnspan=2)
site.focus()
name = Entry(width=42)
name.grid(row=2, column=1, columnspan=2)
name.insert(END, 'garvitagrawal321@gmail.com')
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# Buttons
generate_password = Button(text='Generate Password', width=14, command=password_generator)
generate_password.grid(row=3, column=2)
add = Button(text='Add', width=35, command=save)
add.grid(row=4, column=1, columnspan=2)


screen.mainloop()
