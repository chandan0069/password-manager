from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters + 1)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers + 1)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols + 1)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == '' or email == '' or password == '':
        messagebox.showerror(title="Oops!", message="Don't leave any fields empty.")
    else:
        messagebox.askokcancel(title=website, message=f"These are the details enetered: \nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password} \n")

            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# CANVAS
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(column=1, row=0)

# WEBSITE_LABEL
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# EMAIL/USERNAME LABEL
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "chandanchaudhary1413@gmail.com")

# PASSWORD_LABEL
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# GENERATE PASSWORD BUTTON
password_button = Button(text="Generate Password", width=11, command=generate_password)
password_button.grid(column=2, row=3)

# ADD BUTTON
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()