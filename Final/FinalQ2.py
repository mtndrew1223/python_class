import tkinter as tk #import tk
from tkinter import ttk #import ttk
from tkinter import messagebox #importk messagebox
import csv #import csv module



def read_scores(): #define read scores function
    try: #try statement
        with open('test_data.csv', 'r')as csvfile: #open the csv file
            reader = csv.reader(csvfile) #read the file
            for row in reader: #for statement
                if len(row) >= 3: #if len is greater than three
                    messagebox.showinfo("Read Last Scores from memory", f"Score 1: {row[0]}\nScore 2: {row[1]}\nScore 3: {row[2]}") #message read last scores from memory
                    break #break statement
            else: #else statement
                messagebox.showinfo("No Data", "The file does not contain any data") #ther file doesn't contain any data
    except FileNotFoundError: #except file not found error
        messagebox.showerror("Error", "No CSV file found.") #error message


def calculate_average(): #def function calculate average

    try: #try statement
        score1 = float(entry_1.get())  #score 1
        score2 = float(entry_2.get()) #score 2
        score3 = float(entry_3.get()) #score 3
        
        if score1 < 0 or score1 > 100:#if score 1 is smaller than or greater than 100
            raise ValueError("Score 1 is out of range") #print score 1 is out of range
        elif score2 < 0 or score2 > 100: #elif score is smaller than or greater than 100
            raise ValueError("Score 2 is out of range") #print score 2 is out of range
        elif score3 < 0 or score3 > 100:#elif score is smaller than or greater than 100
            raise ValueError("Score 3 is out of range")#print score 3 is out of range
        else:
            average_score = round((score1 + score2 + score3)/3, 3) #calculate average test score
            messagebox.showinfo("Average Score", f"The average score is {average_score:.3f}") #print the average test score

    except ValueError: #exception
        messagebox.showerror("Input Error", "Please enter valid numeric test scores.") #print error message
        return #return statement
    
    save_button.config(state=tk.NORMAL) #save button to csv
    save_button.config(command=lambda: save_to_csv(score1, score2, score3, average_score))#configure the save button

def save_to_csv(score1, score2, score3, average_score): #define function save to csv
    with open('test_data.csv', 'a', newline='') as csvfile:#open the csv file
        writer = csv.writer(csvfile) #write in the csv file
        writer.writerow([score1, score2, score3, average_score]) #write the scores
    messagebox.showinfo("Saved", "The data has been saved to the CSV file") #print the data has been saved
    save_button.config(state=tk.DISABLED)#disabled save button


root = tk.Tk() #root 
root.title("Average Test Score Calculator") #title of program
root.geometry("400x300") #parameters

frame = ttk.Frame(root, padding="10 10 10 10")  #parameters of frame
frame.pack(fill=tk.BOTH, expand=True) #frame pack

label1 = ttk.Label(frame, text="Enter Test Score 1:") #label 1
label1.grid(column=0, row=0, pady=5, padx=10, sticky=tk.W) #label grid
entry_1 = ttk.Entry(frame) # entry box 
entry_1.grid(column=1, row=0, pady=5, padx=10) #entry box grid

label2 = ttk.Label(frame, text="Enter Test Score 2:") #label 1
label2.grid(column=0, row=1, pady=5, padx=10, sticky=tk.W) #label grid
entry_2 = ttk.Entry(frame) # entry box 
entry_2.grid(column=1, row=1, pady=5, padx=10) #entry box grid


label3 = ttk.Label(frame, text="Enter Test Score 3:") #label 1
label3.grid(column=0, row=2, pady=5, padx=10, sticky=tk.W) #label grid
entry_3 = ttk.Entry(frame) # entry box 
entry_3.grid(column=1, row=2, pady=5, padx=10) #entry box grid

ttk.Button(frame, text="Calculate Average Test Score", command=calculate_average).grid(column=1, row=3, padx=10, pady=10) # button with command

save_button = ttk.Button(frame, text = "Save to CSV", state=tk.DISABLED) #Save to csv button
save_button.grid(column=1, row=4, padx=10, pady=10) #button parameters


ttk.Button(frame, text = "Read scores from file", command = read_scores).grid(column = 1, row = 7, padx = 10, pady = 10) #button to read scores
root.mainloop()#root mainloop