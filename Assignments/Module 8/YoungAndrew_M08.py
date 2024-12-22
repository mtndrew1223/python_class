def display_title(): #define display title functions
    print()    #print space
    print("Andrew Young's Wizard Inventory Game") #print Andrew Young's Wizard Inventory Game
    print() #print space

def display_menu(): #define display menu function
    print("COMMAND MENU") #print command menu
    print() #print space
    print("show - show all items") #print show all items
    print() #print space
    print("grab - Grab an item") #print grab an item
    print() #print space
    print("edit = Edit an item") #print edit an item
    print() #print space
    print("drop - drop an item") #print drop an item
    print() #print space
    print("exit - Exit program") #print exit program
    print() #print space




def show(inventory): #define function
    for number, item in enumerate(inventory, start = 1): #for items section
        print(f"{number}. {item}") #print the number and the item
        print() #print space

def grab_item(inventory): #define grab item inventory
    if len(inventory) >= 4: #if number is bigger than 4
        print("You can't carry any more items. Drop something first! \n") #print you can not carry more items
    else: #else statement
        item = input("Name: ") #name of item
        inventory.append(item) #append inventory
        print(f"{item} was added. \n") #print which item was added

def edit_item(inventory): #define edit inventory
    number = int(input("Number: ")) #pick item
    if number < 1 or number > len(inventory): #if statement
        print("invalid item number.\n") #print invalid number
    else: #else statement
        item = input("Updated name: ") #input new item
        inventory[number-1] = item #inventory
        print(f"Item number{number} was updated. \n") #which item was updated

def drop_item(inventory): #define drop item function
    number = int(input("Number:  ")) # pick which item to drop
    if number < 1 or number > len(inventory): #if statement
        print("Invalid item number. \n") #print invalid number
    else:  #else statement
        item = inventory.pop(number-1) #inventory
        print(f"{item} was dropped. \n") #print which item was dropped


def main():   #define main function
    display_title() #display title
    display_menu() #display menu
    inventory = ["shield" ,  "sword" , "bow"] #show inventory

    while True: #while true command
        command = input("Command:") #input command
        if command == "show": #if statement
            show(inventory) #show inventory
        elif command == "grab":#grab item
            grab_item(inventory) #grab item from inventory
        elif command == "edit": #edit item
            edit_item(inventory) #idet the item
        elif command == "drop": #drop the item
            drop_item(inventory) #drop the item from inventory
        elif command == "exit": #exit from program
            break #break line
        else: #else statement
            print("Not a valid command. Please try again. \n") #print not a vlid statement
    print("Bye!")         #print bye


if __name__ == "__main__": #if name equals main
    main() #main