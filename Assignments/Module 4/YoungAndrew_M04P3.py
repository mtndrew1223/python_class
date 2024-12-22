print("Andrew Young's Change App")
print()

choice = "y"
while choice.lower() == "y":
    #write for loop here to loop through 25,10,5,1
    
    cents = int(input("Enter number of cents 0-99: "))
    print()
    quarters = int(cents//25)
    cents = cents % 25
    dimes = int(cents//10)
    cents = cents % 10
    nickles = int(cents//5)
    pennies = cents % 5

    print("Quarters", quarters)
    print("Dimes" , dimes)
    print("Nickles", nickles)
    print("Pennies", pennies)
    print()



    choice = input("Continue? (y/n)")
print("Bye!")

