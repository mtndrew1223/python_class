#!/usr/bin/env python3
print("Andrew Young Test Results") # Print Andrew Young test results

# display a welcome message
print("The Test Scores program") # Print test scores program
print() # print blanks
print("Enter 3 test scores") # Print enter 3 test scores
print("======================") # Print equal signs

# get scores from the user

score1=int(input("Enter test score: "))#get score 1
score2=int(input("Enter test score: "))#get score 2
score3=int(input("Enter test score: "))#get score 3

total_score= score1 + score2 + score3##add three scores to total score

# total_score = 0       # initialize the variable for accumulating scores
# total_score += int(input("Enter test score: "))
# total_score += int(input("Enter test score: "))
# total_score += int(input("Enter test score: "))

# calculate average score
average_score = round(total_score / 3) # calculate average score
             
# format and display the result
print("======================") #print equal signs

print("Your scores: " + str(score1) + ' ' +  str(score2) + ' ' +  str(score3)) # Calculate lines of scores

print("Total Score:  ", total_score, #print total score
      "\nAverage Score:", average_score) #print average score
print() # print blank
print("Bye") # Goodbye statement


