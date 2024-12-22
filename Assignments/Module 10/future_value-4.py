#!/usr/bin/env python3
        
def get_number(prompt, low, high): #def get_number function
    while True: #while loop
        try: #try statment
            while True: #while statement
                number = float(input(prompt)) #number variable
                if number > low and number <= high: #if statement
                    is_valid = True #is valid = true
                    return number #return the number
                else: #else
                    print(f"Entry must be greater than {low} " #print entry must be greater than low
                        f"and less than or equal to {high}.")
        except ValueError : #exception
            print("Please enter a valid number") #print please enter a valid number
            
def get_integer(prompt, low, high): #define function get integer
    while True: #while loop
        try: # try
            while True: #while true
                number = int(input(prompt)) #number variable
                if number > low and number <= high: #if number  is bigger than low and smaller than high
                    is_valid = True #is valid = true
                    return number #return number
                else: #else statement
                    print(f"Entry must be greater than {low} "  #print entry must be greater than low and less than or equal to high
                        f"and less than or equal to {high}.")
        except ValueError: #exception
            print("Please enter a valid integer") #print please enter a vlid number

def calculate_future_value(monthly_investment, yearly_interest, years): #def dunction calculate future value
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 #calculate monthly interest rate
    months = years * 12 #months = years times 12

    # calculate future value
    future_value = 0.0 #future value variable
    for i in range(months): #for i in range
        future_value += monthly_investment #future value variable
        monthly_interest = future_value * monthly_interest_rate #calculate monthly interest
        future_value += monthly_interest #future value variable

    return future_value #return the future value

def main(): #define main function
    choice = "y" #choice  = y
    while choice.lower() == "y": #while choice  = y
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000) #monthly investment variable
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15) #yearly interest rate variable
        years = get_integer("Enter number of years:\t\t", 0, 50)#years variable

        # get and display future value
        future_value = calculate_future_value( #future value variable then calculate it
            monthly_investment, yearly_interest_rate, years)
        
        print() #print space
        print(f"Future value:\t\t\t{round(future_value, 2)}") #print the future value and round to 2 place
        print() #print space

        # see if the user wants to continue
        choice = input("Continue? (y/n): ") #input if user wants to continue
        print() #print space

    print("Bye!") #print bye
    
if __name__ == "__main__": #if name = main
    main() #main function
