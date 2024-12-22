#!/usr/bin/env python3

tax = 0.06 #sales tax

def sales_tax(total): #start of the function
    return total * tax #return the total * the sales tax

def main():  #main function
    print("Sales Tax Calculator\n") #print Sales Tax Calculator
    total = float(input("Enter total: ")) # Print Enter Total
    total_after_tax = round(total + sales_tax(total), 2) #variable total after tax
    print("Total after tax: $", total_after_tax) #print the total after the sales tax
    
if __name__ == "__main__": #main function
    main() #defining main function
