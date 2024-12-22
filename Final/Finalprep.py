import tkinter as tk #import tk module
from tkinter import ttk    #import ttk module
from tkinter import messagebox #import messagebox module
from datetime import datetime  #import datetime module
import csv

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
    
    save_button.config(state=tk.NORMAL)
    save_button.config(command=lambda: save_to_csv(dob_str, age_in_days))

def save_to_csv(dob_str, age_in_days):
    with open('age_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([dob_str, age_in_days])
    messagebox.showinfo("Saved", "The data has been saved to the CSV file")
    save_button.config(state=tk.DISABLED)

def list_dates():
    try:
        with open('age_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            dates = [row[0] for row in reader]
    except FileNotFoundError:
        messagebox.showerror("Error", "No CSV file found.")
        return
    dates_str = "\n".join(dates)
    messagebox.showinfo("Dates in CSV", f"Dates in the file:\n{dates_str}")

def calculate_average_age():
    try:
        with open('age_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            ages = [int(row[1]) for row in reader if row[1].isdigit()]
    except FileNotFoundError:
        messagebox.showerror("Error", "No CSV file found.")
        return
    if not ages:
        messagebox.showinfo("No Data", "No age data available to calculate the average.")

    average_age_in_days = sum(ages) / len(ages)
    messagebox.showinfo("Average Age", f"The average age in days is {average_age_in_days:.2f} days.")

def enter_another_date():
    entry_1.delete(0, tk.END)
    save_button.config(state=tk.DISABLED)




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

save_button = ttk.Button(frame, text = "Save to CSV", state=tk.DISABLED)
save_button.grid(column=1, row=2, padx=10, pady=10)

ttk.Button(frame, text="List Dates", command=list_dates).grid(column=1, row=3, padx=10, pady=10)

ttk.Button(frame, text="Calculate Average Age", command=calculate_average_age).grid(column=1, row=4, padx=10, pady=10)

ttk.Button(frame, text="Enter Another Date", command=enter_another_date).grid(column=1, row=5, padx=10, pady=10)
root.mainloop()#root mainloop