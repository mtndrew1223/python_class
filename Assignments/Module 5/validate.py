##Andrew Young validations file for the Future Value App

def get_float(prompt,low,high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            return number 
        else: 
            print ("entry must be greater than " +  str(low)  + " and less than or equal to " + str(high))

def get_integer(prompt,low,high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number 
        else: 
            print ("entry must be greater than " +  str(low)  + " and less than or equal to " + str(high))

def main():
    choice = 'y'

    while choice.lower() == 'y':
        valid_number = get_float("Enter Number: ",0 ,1000)
        print("Valid Number:   " + str(valid_number))

        valid_integer = get_float("Enter Number: ",0 ,1000)
        print("Valid Number:   " + str(valid_integer))

        choice = input("Repeat? (y/n):")

if __name__ == "__main__":
    main()