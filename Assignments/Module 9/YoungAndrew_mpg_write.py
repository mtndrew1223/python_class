#!/usr/bin/env python3


import csv #import csv module

FILE_NAME = 'trips.csv' #create files name


def get_miles_driven(): #define miles driven function
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:     #while statement                
        print("Entry must be greater than zero. Please try again.\n")     #print entry must be greater than 0  
    return miles_driven #return statement
          
def get_gallons_used(): #define gallons used functions
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:       #while statement              
        print("Entry must be greater than zero. Please try again.\n") #print entry must be greater than 0
    return gallons_used #return gallons used function
        
def main(): #main functiuon
    # display a welcome message
    print("The Miles Per Gallon program")
    print() #print space

    #Create List
    trips = []

    more = "y" #more variable
    while more.lower() == "y": #while statement
        miles_driven = get_miles_driven() #miles driven 
        gallons_used = get_gallons_used()#gallons used
                                 
        mpg = round((miles_driven / gallons_used), 2) #mpg variable
        print(f"Miles Per Gallon:\t{mpg}") #print miles per gallon
        print() #print space

        trips.append([miles_driven, gallons_used, mpg]) #append trip
       
        
        more = input("More entries? (y or n): ") #more variable

        #send list to file
    with open(FILE_NAME, "w", newline='') as output_file: #open statement
        writer = csv.writer(output_file) #writer variable
        writer.writerows(trips) #write the different rows
        print("Bye!") #bye

if __name__ == "__main__": #if name equals main
    main() #main function

