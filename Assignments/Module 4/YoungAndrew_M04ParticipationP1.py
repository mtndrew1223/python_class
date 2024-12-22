#!/usr/bin/env python3

# display a welcome message
print("Andrew Young's Miles Per Gallon Application") #name of appication
print() #blank space

another_trip = 'y' #variable another trip

while another_trip.lower() == 'y' : #make while statement
    # get input from the user
    miles_driven    = float(input("Enter miles driven:         ")) #create variable miles driven
    gallons_used    = float(input("Enter gallons of gas used:  ")) #create variable gallons used
    cost_per_gallon = float(input("Enter Cost per Gallon:      ")) #create variable cost per gallon

    if miles_driven <= 0: #create if statement
        print("Miles driven must be greater than zero. Please try again.") #print miles driven must be greater than 0
    elif gallons_used <= 0:#create elif 
        print("Gallons used must be greater than zero. Please try again.")#print error message
    elif cost_per_gallon <= 0: #create elif 
        print("Cost per Gallon must be greater than zero. Please try again.") #create error message
    else: #make else statement
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2) #calcualte miles per gallon
        total_cost = gallons_used * cost_per_gallon #calculate total cost
        cost_per_mile = total_cost / miles_driven #calculate cost per mile

        print("Miles Per Gallon:          ", mpg) #print miles per gallon
        print("Total Cost:                ", round(total_cost, 2)) #print total cost of trip
        print("Cost per Mile:             ", round(cost_per_mile, 2)) # print total cost per mile
        print() #print blank space
        another_trip = input("Do you want to enter another trip? (y/n): ") #creat another trip variable
        print() #print blank space

print("Bye") #print goodbye statement




