import tkinter as tk #import tk module
from tkinter import ttk #import ttk module
from tkinter import messagebox #import messagebox module


def calculate_hypotenuse(): #define calculate function
    side_1 = entry_1.get() #get entry 1
    side_2 = entry_2.get() #get entry 2

    if not side_1 or not side_2: #if statement about the values
        messagebox.showerror("Input Error" "Please enter values for both sides.") #messagbox show error
        return #return statement

    side_1 = float(side_1) #convert value to float
    side_2 = float(side_2) #convert value to float

    if side_1 <=0 or side_2 <= 0: #if statement about the validity of the numbers
        messagebox.showwarning("Input Error", "Please enter positive numbers") #messagebox error
        return# return statement
    
    hypotenuse = (side_1 **2 + side_2 **2)**0.5#hypotenuse variable
    hypotenuse = round(hypotenuse, 3) #round the hypotenuse to 3 decimal points
    result_var.set(f"{hypotenuse:.3f}") #set sypotenuse




root = tk.Tk() #root variable
root.title ("Right Triangle Calculator") #title of Gui application
root.geometry("350x300") #how big the window is

frame = ttk.Frame(root, padding= "10 10 10 10") #frame parameters
frame.pack(fill=tk.BOTH, expand = True) #frame pack


label1 = ttk.Label(frame, text = "Enter length of first side:") #1st label
label1.grid(column = 0, row = 0, pady = 20, padx = 10, sticky = tk.W) #1st label grid

label_2 = ttk.Label(frame, text = "Enter length of second side:") #2nd label
label_2.grid(column = 0, row = 1, pady = 20, padx = 10, sticky = tk.W) #2nd label grid

entry_1 = ttk.Entry(frame) #entry box 1
entry_1.grid(column=1, row=0, pady=20, padx=10) #entry box 2 grid whereabouts

entry_2 = ttk.Entry(frame) #entry box 2
entry_2.grid(column=1, row = 1, pady = 20, padx = 10) #entry box 2 grid whereabouts

result_var = tk.StringVar() #get the results!
result_label = ttk.Label(frame, textvariable=result_var) # set label
result_label.grid(column=0, row = 3, columnspan=2, pady=10) #where abouts of the answer


ttk.Button(frame, text = "Calculate Answer", command=calculate_hypotenuse).grid(column = 1, row = 2, padx = 10, pady = 10) #button to calculate

root.mainloop() #mainloop function





