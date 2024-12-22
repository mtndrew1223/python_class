#!/usr/bin/env python3

def display_welcome(): #define welcome function
    print("The Test Scores program") #print the test scores program
    print("Enter 'x' to exit") #enter x to exit
    print("") #print space

def get_scores(): #define function get scores
    scores = [] #scores list
    while True: #while statement
        score = input("Enter test score: ") #score variable
        if score == "x": #if statement
            return scores #return score
        else: #else statement
            score = int(score) #score variable
            if score >= 0 and score <= 100: #if statement
               scores.append(score) #scores append
            else: #else statement
                print("Test score must be from 0 through 100. " + #print test scores must be from 0 to 100
                      "Score discarded. Try again.") #print scores discarded, please try again

def process_scores(scores): #define process scores function
    scores.sort() #scores sort
    # calculate numbers

    score_total = sum(scores) #score total variable
    count = len(scores) #count the scores
    average = score_total / count #find the average
    low = min(scores) #find the lowest score
    high = max(scores) #find the highest score

    #calculate median index

    median_index = len(scores) // 2 #find the median index
    if len(scores) % 2 == 0: #if statement
        median = (scores[median_index] + scores[median_index - 1]) / 2 #find the median
    else: #else statement
        median  = scores[median_index] #median
                
    # format and display the result
    print() #print space
    print("Score total:       ", score_total) #print score total
    print("Number of Scores:  ", count) #print number of scores
    print("Average Score:     ", average) #print the average score
    print("Low Score    :     ", low) #print the lowest score
    print("High Score   :     ", high) #print the highest score
    print("Median Score :     ", median) #print the median score
    #low score
    #high score
    #median score

def main(): #define main function
    display_welcome() #display the welcome statement
    scores = get_scores() #get the score
    process_scores(scores) #process the scores
    print("") #print space
    print("Bye!") #print bye

# if started as the main module, call the main function
if __name__ == "__main__": #main funcion
    main() #main


