#!/usr/bin/env python3

import csv #import csv module

FILE_NAME = 'trips.csv' #name file

def write_trips(trips): #define function writer trips

     with open(FILE_NAME, "w", newline='') as output_file: #open file
        writer = csv.writer(output_file) #define writer variable
        writer.writerows(trips) #write the trips

def read_trips(): #define function read trips
    trips = [] #make trips list
    with open(FILE_NAME, "r", newline = '') as input_file: #open and read file
        reader = csv.reader(input_file) #define reader variable
        for row in reader: #for statement
            trips.append(row) #append trips row

    return trips #return

def list_trips(trips): #define list trips function
    print("Dist\tGallons\tMPG") #print distance gallons and mpg
    for i in range (0, len(trips)): #create range
        trip = trips[i] #trip variable
        print (str(trip[0]) + '\t' + str(trip[1]) + '\t' + str(trip[2])) #print the trips
    print() #print space

def get_miles_driven(): #define miles driven function
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0: #while statement                    
        print("Entry must be greater than zero. Please try again.\n")    #print entry must be greater than 0   
    return miles_driven #return statement
          
def get_gallons_used(): #define gallons used function
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:   #while statement                 
        print("Entry must be greater than zero. Please try again.\n") #print entry must be greater than 0
    return gallons_used #return gallons used

def main(): #main function
    # display a welcome message
    print("The Miles Per Gallon program")
    print() #print space

    trips = read_trips()
    list_trips(trips)

    more = "y" #more variable
    while more.lower() == "y": #while statement
        miles_driven = get_miles_driven() #miles driven variable
        gallons_used = get_gallons_used() #gallons used variable


        mpg = round((miles_driven / gallons_used), 2) #mpg variable
        
        single_trip = [miles_driven, gallons_used, mpg]
        trips.append(single_trip)

        print(f"Miles Per Gallon:\t{mpg}") #print miles per gallon
        print() #print space
        
        more = input("More entries? (y or n): ") #ask user if they want to input more entries
    
    write_trips(trips)
    list_trips(trips)
    
    print("Bye!") #goodbye statement

if __name__ == "__main__": #if name equals main
    main() #main

