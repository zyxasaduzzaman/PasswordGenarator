import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import string


def generate_password():
    try:
        length = int(entry_size.get())
        if length < 1:
            raise ValueError("Length must be at least 1")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")


def copy_to_clipboard():
    password = entry_password.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")



root = tk.Tk()
root.title("Password Generator")
root.geometry("650x400+400+200")
root.configure(bg="SpringGreen3")
root.resizable(False, False)


frame = tk.Frame(root, bg="SpringGreen1", width=590, height=230)
frame.place(x=30, y=70)


label_title = tk.Label(root, text="Password Generator Application", font=("arial", 30, "bold", "italic"), bg="SpringGreen3", fg="white")
label_title.place(x=20, y=10)


label_size = tk.Label(frame, text="Enter password size", font=("arial", 20, "bold"), fg="brown", bg="SpringGreen1")
label_size.place(x=150, y=5)
entry_size = tk.Entry(frame, width=18, font=("arial", 20, "bold"))
entry_size.place(x=150, y=50)
entry_size.insert(0,"12")


label_password = tk.Label(frame, text="Your password", font=("arial", 20, "bold"), fg="brown", bg="SpringGreen1")
label_password.place(x=180, y=100)
entry_password = tk.Entry(frame, width=70, font=("arial", 10, "bold"))
entry_password.place(x=50, y=150, height=40)

button_generate = tk.Button(root, text="Generate", font=("arial", 20, "bold"), bg="lightblue", fg="black", command=generate_password)
button_generate.place(x=120, y=320)

button_copy = tk.Button(root, text="Copy", font=("arial", 20, "bold"), bg="lightblue", fg="black", command=copy_to_clipboard)
button_copy.place(x=400, y=320)

root.mainloop()
