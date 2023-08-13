import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    strings = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(strings) for _ in range(length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)

def accept_password():
    accepted_password = password_output.get()

def reset_password():
    length_entry.delete(0, tk.END)
    password_output.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")

frame = tk.Frame(root)
frame.pack(pady=20)

passwordgenerator_label = tk.Label(frame, text= "PASSWORD GENERATOR", font=("bold italic",16), fg="green")
passwordgenerator_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

username_label = tk.Label(frame, text="Enter Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(frame, width=20, font=("times",14))
username_entry.grid(row=1, column=1, padx=10, pady=10)

length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=2, column=0, padx=10, pady=10)
length_entry = tk.Entry(frame, width=20, font=("times", 14))
length_entry.grid(row=2, column=1, padx=10, pady=10)

generated_password_label = tk.Label(frame, text="Generated Password:", font=("times", 14))
generated_password_label.grid(row=3, column=0, padx=10, pady=10)
password_output = tk.Entry(frame, font=("times", 14))
password_output.grid(row=3, column=1, padx=10, pady=10)

generate_button = tk.Button(frame, text= "GENERATE", font=("times",14), command= generate_password)
generate_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2 )

accept_button = tk.Button(frame, text="ACCEPT", font=("times",14), command=accept_password)
accept_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

reset_button = tk.Button(frame, text="RESET", font=("times",14), command=reset_password)
reset_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)
root.title("This Application is Made By Dhiraj")
root.mainloop()
