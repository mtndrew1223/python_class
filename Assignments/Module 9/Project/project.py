import csv #import csv module

FILE_NAME = "monthly_sales (1).csv" #name file


def display_title(): #define function diplay title
    print("Andrew Young's Monthly Sales") #print andrew young's monthly sales
    print()#print space

def display_menu(): #define function display menu
    print("COMMAND MENU") #print COMMAND MENU
    print() #print space
    print("monthly - View monthly sales") #print monthly-view monthly sales
    print() #print space
    print("yearly - View yearly summary") #print yearly-view yearly summary
    print() #print space
    print("edit - Edit sales for a month") #print edit-edit sales for a month
    print()#print space
    print("exit - Exit program") #print exit-exit program
    print() #print space



def read_sales(): #def read sales function
    sales = [] #sales list
    try: #exception statement
        with open(FILE_NAME, newline = "") as file: #open the file
            reader = csv.reader(file) #read the file
            for row in reader: #for statement
                sales.append(row) #append sales row
    except FileNotFoundError: #exception, if file is not found
        sales = [["Jan", "0",], ["Feb", "0"], ["Mar", "0"], ["Apr", "0"], ["May", "0"],["Jun", "0"], ["Jul", "0"], ["Aug", "0"], ["Sep", "0"], ["Oct", "0"], ["Nov", "0"], ["Dec", "0"]] #amount of sales
        write_sales(sales) #call write sales function
    return sales #return sales


def view_monthly_sales(sales): #define function view monthly sales
    for row in sales: #for statement
        print(f"{row[0]} - {row[1]}") #print the sales
    print() #print space

def view_yearly_summary(sales): #define function view yearly summary
    total = 0 #total = 0
    for row in sales: #for statement
        amount = int(row[1]) #amount integer
        total += amount #total

    count = len(sales) #count sales
    if count == 0: #if statement
        print("No sales data available to calculate yealy summary") #print there is no sales data
        return #return
    average = total / count #calculate the average
    average = round(average, 2) #round the average to 2

    print("Yearly total:    ", total) #print the yearly total
    print("Monthly average:     ", average) #monthly average
    print() #print space


def edit(sales): # Define the edit function 
    names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] # List of month abbreviations 
    name = input("Select a Month: ").title() # Get user input for the month and capitalize it 
    if name not in names: # Check if the month is valid 
        print("Invalid three-letter month") # Print an error message if invalid 
    else:
        index = names.index(name) # Get the index of the month 
        while True: #while statement
            try: #try statement
                amount = int(input("Sales Amount: ")) # Get user input for the sales amount 
                break
            except ValueError:
                print("Invalid input")
        month = [name, str(amount)] # Create a new month entry 
        sales[index] = month # Update the sales list at the correct index 
        write_sales(sales) # Call the write_sales function 
        print(f"Sales amount for {month[0]} was modified.") # Print a success message 
        print() # Print a space

def write_sales(sales): #define write sales function
    with open(FILE_NAME, "w", newline = "") as file: #open the file
        writer  = csv.writer(file) #write within the file
        writer.writerows(sales) #write the row

def main(): #def main function
    display_title() #display title
    display_menu() #display menu
    sales = read_sales() #sales variable
    
    while True: #while statement
        command = input("Command: ") #input command
        if command == "monthly": #if command is monthly
            view_monthly_sales(sales) #view monthly sales 
        elif command == "yearly": #elif command is yearly
            view_yearly_summary(sales) #view yearly summary
        elif command  == "edit": #elif command is edit
            edit(sales) #edit sales
        elif command == "exit": #elif command is exit
            break #break statement
        else: #else
            print("Not a valid command. Please try again!\n") #print not a vlid statement
    print("Bye!") #print bye


if __name__ == "__main__": #if name = main
    main() #main function