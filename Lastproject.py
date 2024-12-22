import csv #import csv module

FILENAME = "contacts.csv" #name of file

def display_title(): #def display title function
    print("Andrew Young's Contact Manager App") #print statement
    print() #print space

def display_menu(): #def display menu function
    print("COMMAND MENU") #print command menu
    print() #print space
    print("list - display all contacts") #print list
    print()#print space
    print("view - view all contacts") #print view
    print()#print space
    print("add - Add a contact") #print add
    print()#print space
    print("del - Delete a contact") #print del
    print()#print space
    print("exit - Exit Program") #print exit
    print()#print space

def read_contacts(): #def read contacts function
    contacts = [] #contacts list
    try: #try statement
        with open(FILENAME, newline = "") as file: #open the file
            reader  = csv.reader(file) #read the file
            for row in reader: #for statement
                contacts.append(row) #append contacts
    except FileNotFoundError: #exception statement
        print("Could not find contacts file! Starting new contacts file...") #print error statement
    return contacts #return statement

def display(contacts): #def display function
    if len(contacts)== 0: #if statement
        print("There are no contacts in the list") #print there are not contacts in list
        return #return statement
    for i, row in enumerate(contacts, start=1): #for statement
        print(f"{i}. {row[0]}") #print the contacts
    print() #print space
    
def view(contacts): #define view function
    number = get_contact_number(contacts) #the the number of contacts
    if number > 0: #if number is greater than 0
        contact = contacts[number-1] #contatc variable
        print("Name:", contact[0]) #print name
        print("Email:", contact[1]) #print email
        print("Phone:", contact[2]) #print phone
        print() #print space
        
def get_contact_number(contacts): #def get contact number function
    while True: #while statement
        try: #try statement
            number = int(input("Number:")) #number variable
        except ValueError: #exception
             print("Invalid integer. \n") #print invalid integer
             return -1 #return
        if number < 1 or number > len(contacts): #if number is smaller than 1
             print("Invalid contact number. \n") #print error statement
             return -1 #return statement
        else: #else
             return number #return the variable
        
def add(contacts): #def function add onctacts
    name = input("Name: ") #input name
    email = input("Email: ") #input email
    phone = input("Phone: ") #input phone
    contact = [name, email, phone] #list name email phone
    contacts.append(contact) #append contact
    write_contacts(contacts)#call write contacts function
    print(f"{name} was added") #print the name was added
    print() #print space

def write_contacts(contacts): #def write contacts function
     with open (FILENAME, "w", newline = "") as file: #open file
          writer = csv.writer(file) #writer variable
          writer.writerows(contacts) #variable and function

def delete(contacts): #def delete contacts function
    number = get_contact_number(contacts) #number variable
    if number > 0: #if statement
        contact = contacts.pop(number-1) #conact pop
        print(f"{contact[0]} was deleted. \n") #print while contact was deleted
    write_contacts(contacts) #call write contacts function


def main(): #def main function
    contacts = read_contacts() #variable contacts is equal to read contacts
    display_title() #call display title function
    display_menu() #call display menu function
    
    while True: #while statement
        command = input("Command: ") #command variable
        if command  == "list": #if command is list
            display(contacts) #call display function
        elif command == "view": #elif command is view
            view(contacts) #call view function
        elif command == "add": #elif command is add
            add(contacts) #call add function
        elif command  == "del": #elif command is del
            delete(contacts) #call delete function
        elif command == "exit": #elif command is exit
            break #break statment
        else: #else
            print("Not a valid command. Please try again. \n") #print error statement
    print("Bye!") #print bye


if __name__ == "__main__": main() #if name = main