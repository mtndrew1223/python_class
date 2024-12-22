import tkinter as tk #this will become an object
from tkinter import ttk

def click_button1():
    #counter += 1
    test_window.title("You clicked the button")


def click_button2():
    test_window.destroy()

test_window = tk.Tk() #this will create the window, and windows run in loops
test_window.title("Test App")
test_window.geometry("500x300")



button1 = ttk.Button(frame, text="Click Me!", command=click_button1)
button1.pack()
button2 = ttk.Button(frame, text = "No Click Me!", command=click_button2)
button2.pack()

label1 = ttk.Label(frame, text= "Test Label").pack()
entry_text1 = tk.StringVar()
entry1 = ttk.Entry(frame, width=25, textvariable = entry_text1).pack()

test_window.mainloop() #this function keeps the window open and open the window