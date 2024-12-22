import tkinter as tk #import tk module
from tkinter import ttk    #import ttk module
from tkinter import messagebox #import messagebox module
from datetime import datetime  #import datetime module


def calculate_age(): #define calculate age function
    dob_str = entry_1.get() # get day of birth
    if not dob_str: # if statement
        messagebox.showerror("Input Error", "Please enter your date of birth.") #messagebox error
        return #return statement
    
    try: #try statement
        dob = datetime.strptime(dob_str, "%Y-%m-%d") #dob variable
    except ValueError: #except statement
        messagebox.showerror("Input Error", "Date format should be YYYY-MM-DD.") #messagebox error
        return # return statement
    
    today = datetime.today() #today variable
    age_in_days = (today - dob).days  #calculate age in days

    messagebox.showinfo("Age in Days", f"You are {age_in_days} days old.") #messagebox error


root = tk.Tk() #root 
root.title("Days Old Calculator") #title of program
root.geometry("400x300") #parameters

frame = ttk.Frame(root, padding="10 10 10 10")  #parameters of frame
frame.pack(fill=tk.BOTH, expand=True) #frame pack

label1 = ttk.Label(frame, text="Enter your date of birth (YYYY-MM-DD):") #label 1
label1.grid(column=0, row=0, pady=20, padx=10, sticky=tk.W) #label grid

entry_1 = ttk.Entry(frame) # entry box 
entry_1.grid(column=1, row=0, pady=20, padx=10) #entry box grid

ttk.Button(frame, text="Calculate Age", command=calculate_age).grid(column=1, row=1, padx=10, pady=10) # button with command




root.mainloop()#root mainloop


