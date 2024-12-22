#!/usr/bin/env python3
print('Andrew Young MPG App') #Intro statement
print()  #blank

# display a welcome message
print("The Miles Per Gallon program") #Introducing the program
print() #print blank

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t")) #enter miles driven
gallons_used = float(input("Enter gallons of gas used:\t")) #enter gallons of gas used
gallon_cost= float(input("Enter cost per gallon:\t\t")) #enter cost per gallon


# do calculations
mpg = round(miles_driven / gallons_used, 1) #calculating miles per gallon
gas_cost= round(gallons_used * gallon_cost, 1) #Calculate cost of gas
mile_cost = round(gas_cost / miles_driven, 1) #Calculate cost per mile

            
# format and display the result
print() #print blank
print("Miles Per Gallon:\t\t" + str(mpg)) #print out Miles per gallon
print("Total Gas Cost:\t\t\t" + str(gas_cost))##Print total cost of gas
print("Cost Per Mile:\t\t\t" + str(mile_cost)) ##print cost per mile

print() #print blank
print("Bye") #goodbye message


