import csv #import csv module
import sys #import sys module

FILENAME = "movies.csv" #name the file

def exit_program(): #def exit prgram
    print("Terminating program.") #print terminating program
    sys.exit() #exit the program

def read_movies(): #define read movies function
    try: #try statement
        movies = [] #movies list
        with open(FILENAME, newline="") as file: #open the file
            reader = csv.reader(file) #read the file
            for row in reader: #for statement
                movies.append(row) #append the movies
        return movies #return statement
    except FileNotFoundError as e: #exception
        print(f"Could not find {FILENAME} file. Making new one") #print file not found
        return [] #create new file
    except Exception as e: #exception
        print(type(e), e) #print error statement
        exit_program() #exit program

def write_movies(movies): #define write movies function
    try: #try statement
        #raise BlockingIOError("test Blocking IOError")
        with open(FILENAME, "w", newline="") as file:  #open the file
            writer = csv.writer(file) #write within the file
            writer.writerows(movies) #write
    except OSError as e: #exepction
        print("OSError Found") #print OSError found
        print(type(e), e) #print the type of error
        exit_program #exit program
    except Exception as e: #exception statement
        print(type(e), e) #print the type of error
        exit_program() #exit the program

def list_movies(movies): #def function list movies
    for i, movie in enumerate(movies, start=1): #for statement
        print(f"{i}. {movie[0]} ({movie[1]})") #print the movies
    print() #print space
    
def add_movie(movies): #define function add movie
    name = input("Name: ") #input the name of the movie
    while True: #while true statement
        try: #try statement
            year = int(input("Year: ")) #input year
            if year <= 0: #if the year is smaller than 0
                raise ValueError #raise the value error
            movie = [name, year] #list the movie
            movies.append(movie) #append the movies
            write_movies(movies) #write movies function
            print(f"{name} was added.\n") #print which movie was added 
            return #return statement
        except ValueError: #exception statement
            print("Please enter a valid year") #print please enter a valid year

def delete_movie(movies): #define delete movie function
    while True: #while true statement
        try: #try statement
            number = int(input("Number: ")) #input Number
        except ValueError: #exception statement
            print("Invalid integer. Please try again.") #print invalid integer
            continue #continue statement
        if number < 1 or number > len(movies): #if statement
            print("There is no movie with that number. Please try again.") #print there is no movie with that number
        else: #else 
            break #break statement
    movie = movies.pop(number - 1) #movie 
    write_movies(movies) #call write movies function
    print(f"{movie[0]} was deleted.\n") #print which movies are  deleted

def display_menu(): #define display menu function
    print("The Movie List program") #print the movie lsit program
    print() #print space
    print("COMMAND MENU")#print COMMAND MENU
    print("list - List all movies") #print list all movies
    print("add -  Add a movie") #print add a movie
    print("del -  Delete a movie") #print delete a movie
    print("exit - Exit program") #print exit program
    print()    #space

def main(): #print main function
    display_menu() #lcall display menu function
    movies = read_movies() #movies variable
    while True:       #while true statement  
        command = input("Command: ") #command input
        if command.lower() == "list": #if the command is list
            list_movies(movies) #list movies
        elif command.lower() == "add":#elif command is ass
            add_movie(movies) #add movies
        elif command.lower() == "del": #elif command is del
            delete_movie(movies) #delete the movie
        elif command.lower() == "exit": #elif command is exit
            break #break
        else: #else
            print("Not a valid command. Please try again.\n") # print not a valid command
    print("Bye!") #print bye

if __name__ == "__main__": # if name = main
    main() #main function
