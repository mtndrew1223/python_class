import tkinter as tk  #import tkinter module
from tkinter import ttk, messagebox #import tk
def show_message(): #define function show message
    name = name_entry.get() #name variable
    if name: messagebox.showinfo("Greeting", f"Hello, {name}!") #if statement
    else: messagebox.showwarning("Input Error", "Please enter a name.") #else statement



root = tk.Tk() #root
root.title("Simple App") #title of app, Simple App
root.geometry("300x150") #how big the application will be 

ttk.Label(root, text="Enter your name:").grid(column=0, row=0, padx=10, pady=10)#User enters name
name_entry = ttk.Entry(root, width=20) #name entry variable
name_entry.grid(column=1, row=0, padx=10, pady=10)#where the name entry is located

ttk.Button(root, text="Greet", command=show_message).grid(column=1, row=1, padx=10, pady=10)#make the button

root.mainloop() #main loop