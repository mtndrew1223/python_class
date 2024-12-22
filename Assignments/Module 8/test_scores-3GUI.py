#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



def display_welcome():
    print("The Test Scores program")
    print("Enter x to exit")
    print()

def get_scores(): #define function get scores
    score = entry1.get() #scores list
    if score == "x": #if statement
        return scores #return score
    else: 
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 100:
                scores.append(score)
                entry1.delete(0, tk.END)
            else:
                messagebox.showwarning("input error")
        else:
            messagebox.showwarning("input Error", "Please enter valid test scores")

def process_scores(scores): #define process scores function
    scores.sort() #scores sort
    # calculate numbers

    score_total.set(f"Score total:  {sum(scores)}") #score total variable
    number_of_scores.set(f"Number of Scores": {len(scores)}" )
    average_score.set(f"Average Score:  {sum(scores) / len(scores):.2f}")
    low_score.set(f"Low Score:    {min(scores)}")
    high_score.set(f"High Score:  {max(scores)}")

    #calculate median index

    median_index = len(scores) // 2 #find the median index
    if len(scores) % 2 == 0: #if statement
        median = (scores[median_index] + scores[median_index - 1]) / 2 #find the median
    else: #else statement
        median  = scores[median_index] #median
    median_score.set(f"Median Score:  {median:.2f}")
                
root = tk.Tk()
root.title("The Test Scores Program")
root.geometry("350x300")

frame = ttk.Frame(root, padding= "10 10 10 10")
frame.pack(fill=tk.BOTH, expand = True)

label1 = ttk.Label(frame, text = "Enter Test Score: ")
label1.grid(column = 0, row = 0, pady = 20, padx = 10, sticky = tk.W)

entry1 = ttk.Entry(frame)
entry1.grid(column=1, row = 0, pady = 20, padx = 10)


ttk.Button(frame, text = "Add Score" , command = get_scores).grid(column = 0, row = 1 , padx = 10, pady = 10)
ttk.Button(frame, text = "Calculate Scores", command=process_scores).grid(column = 1, row = 1, padx = 10, pady = 10) #make sure this line is correct

scores = []

score_total = tk.StringVar()
number_of_score = tk.StringVar()
low_score = tk.StringVar()
high_score = tk.StringVar()
median_score = tkStringVar()

score_total_label = ttk.Label(frame, textvariable = score_total)
score_total_label.grid(column = 0, row = 2, columnspan = 2, pady = 10)

number_of_score_label = ttk.Label(frame, textvariable = number_of_score)
number_of_score_label.grid(column = 0, row = 3, columnspan = 2, pady = 10)

low_score_label = ttk.Label(frame, textvariable = low_score)
low_score_label.grid(column = 0, row = 4, columnspan = 2, pady = 10)

high_score_label = ttk.Label(frame, textvariable = high_score)
high_score_label.grid(column = 0, row = 5, columnspan = 2, pady = 10)

median_score_label = ttk.Label(frame, textvariable = median_score)
median_score_label.grid(column = 0, row = 6, columnspan = 2, pady= 10)




root.mainloop()