import tkinter as tk
from tkinter import ttk

def change_title():
    root.title(entry_text.get())

root = tk.Tk()


window = tk()
window.geometry("500x250")
entry_text = tk.StringVar()
entry = ttk.Entry(root, width=25, textvariable=entry_text).pack()
button = ttk.Button(entry, text="Change Title", command=change_title).pack()

tk.mainloop()