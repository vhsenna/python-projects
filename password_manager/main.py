from tkinter import messagebox, Tk, Canvas, PhotoImage, Label, Entry, Menu, Button, END
from random import choice, randint, shuffle
import pyperclip
import json


# ----- Password Generator ----- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ----- Save Password ----- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please make sure you haven\'t left any fields empty.')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n\nUsername: {username} '
                                                              f'\nPassword: {password}\n\nIs it ok to save?')
        if is_ok:
            try:
                with open('data/data.json', 'r') as data_file:
                    data = json.load(data_file)
                    if website in data:
                        update = messagebox.askyesno('Warning', f'There is already a password saved for {website}.\n\n'
                                                                f'Would you like to overwrite?')
                        if update:
                            data[website]['password'] = password
                            data[website]['username'] = username
                        else:
                            return
                    else:
                        data.update(new_data)

                    data.update(new_data)
            except FileNotFoundError or json.decoder.JSONDecodeError:
                with open('data/data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
                pass
            else:
                with open('data/data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def put_default():
    try:
        with open('data/data.json') as file:
            data = json.load(file)
            if len(data) != 0:
                for website in data:
                    username_entry.delete(0, END)
                    username_entry.insert(END, data[website]['username'])
    except FileNotFoundError or json.decoder.JSONDecodeError:
        username_entry.delete(0, END)
        username_entry.insert(END, 'example@email.com')


# ----- Find Password ----- #
def search():
    website = website_entry.get()
    if len(website) != 0:
        try:
            with open('data/data.json') as file:
                data = json.load(file)
            password = data[website]['password']
            username = data[website]['username']
        except FileNotFoundError:
            messagebox.showwarning('File not found Error', 'No data file found.\n\nSolution: Please add some data and save passwords to search.')
        except KeyError:
            if website[0] == ' ':
                messagebox.showerror('Error', 'Please enter valid data to search.\nSearch with exact website name without any spaces.')
            else:
                messagebox.showerror('Error', 'The website you searched for is not added to our database.')
        else:
            pyperclip.copy(password)
            message = f'Username: {username}\nPassword: {password}\n\nYour password is copied to clipboard.'
            messagebox.showinfo(website, message)


# ----- Menu Functions ----- #
def format_data(new_window):
    pass_buttons = []
    passwords = []
    usernames = []
    websites = []
    web_y = 30
    em_y = 30
    pas_y = 30
    pass_btn_width = 0
    try:
        with open('data/data.json') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError or FileNotFoundError:
        if_no = Label(new_window, text='No Saved Data or Passwords found\nAdd Passwords to view them.', bg='white')
        if_no.place(x=110, y=90)
    else:
        for website in data:
            websites.append(website)
            usernames.append(data[website]['username'])
            passwords.append(data[website]['password'])
        for pw in passwords:
            if len(pw) > pass_btn_width:
                pass_btn_width = len(pw)
        for website in websites:
            websites_label = Label(new_window, text=website, bg='white')
            websites_label.place(x=10, y=web_y)
            web_y += 30
        for username in usernames:
            usernames_label = Label(new_window, text=username, bg='white')
            usernames_label.place(x=130, y=em_y)
            em_y += 30

        def copy_pass(password_to_copy):
            pyperclip.copy(password_to_copy)

        for password in passwords:
            pas_button = Button(new_window, text=password, height=1, width=pass_btn_width, bg='white')
            pas_button.config(command=lambda password_arg=pas_button: copy_pass(password_arg.cget('text')))
            pas_button.place(x=300, y=pas_y)
            pas_y += 30
            pass_buttons.append(pas_button)

    new_window.mainloop()


def view_saved():
    new_window = Tk()
    new_window.geometry('480x200')
    new_window.config(bg='white')
    new_window.title('Saved Passwords')
    user_label = Label(new_window, text='Website', font=('Arial', 10, 'bold'), bg='white')
    user_label.place(x=10, y=10)
    username_label = Label(new_window, text='Username', font=('Arial', 10, 'bold'), bg='white')
    username_label.place(x=150, y=10)
    pas_label = Label(new_window, text='Password', font=('Arial', 10, 'bold'), bg='white')
    pas_label.place(x=300, y=10)
    format_data(new_window)


# ----- UI Setup ----- #
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40, bg='white')

# Canvas
canvas = Canvas(height=200, width=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file='img/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, sticky='EW')

# Labels
website_label = Label(text='Website', bg='white', font=('Arial', 10))
website_label.grid(row=1, column=0, padx=(0, 15), sticky='EW')
username_label = Label(text='Username', bg='white', font=('Arial', 10))
username_label.grid(row=2, column=0, padx=(5, 10), sticky='EW')
password_label = Label(text='Password', bg='white', font=('Arial', 10))
password_label.grid(row=3, column=0, padx=(0, 6), sticky='EW')

# Entries
website_entry = Entry(width=25, font=('Arial', 8))
website_entry.grid(row=1, column=1, sticky='EW')
website_entry.focus()
username_entry = Entry(width=20, font=('Arial', 8))
username_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
put_default()
password_entry = Entry(width=25, font=('Arial', 8))
password_entry.grid(row=3, column=1, sticky='EW')

# Buttons
search_button = Button(text='Search', width=13, font=('Arial', 10), command=search)
search_button.grid(row=1, column=2, padx=(5, 0), pady=(5, 5), sticky='EW')
generate_password_button = Button(text='Generate Password', font=('Arial', 10), command=generate_password)
generate_password_button.grid(row=3, column=2, padx=(5, 0), pady=(5, 5), sticky='EW')
add_button = Button(text='Add', width=36, font=('Arial', 10), command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

# Menu Bar
menu_bar = Menu(window)
options = Menu(menu_bar, tearoff=0)
options.add_command(label='Saved Passwords', command=view_saved)

options.add_separator()
options.add_command(label='Exit', command=window.quit)

menu_bar.add_cascade(label='Options', menu=options)
window.config(menu=menu_bar)
print(window.winfo_height(), window.winfo_width())

window.mainloop()
