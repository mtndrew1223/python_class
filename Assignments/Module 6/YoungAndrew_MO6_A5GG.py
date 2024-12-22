#!/usr/bin/env python3

import random #import random module

def display_title(): #display title function
    print("Guess the number!") #print guess the number
    print() #print blank space

def get_limit(): #define function get limit
    limit = int(input("Enter the upper limit for the range of numbers: ")) #limit vaariable
    return limit #return the limit

def play_game(limit): #define function play game
    number = random.randint(1, limit) #number variable
    print(f"I'm thinking of a number from 1 to {limit}\n") #print I'm thinking of a number
    count = 0 #count statement

    while True: #while statement
        guess = int(input("Your guess: ")) #input users guess
        count += 1 #count the number of tries
        if guess < number: #if statement
            print("Too low.")  #print too low statement
        elif guess > number: #elif statement
            print("Too high.")  #print too high
        else: #else statement
            print(f"You guessed it in {count} tries.\n") #print how many tries it took for the user to guess correctly
            return #return statement

def main(): #main function
    display_title() #title
    again = "y" #again choice
    while again.lower() == "y": #while statement
        limit = get_limit() #limit variable
        play_game(limit) #play game variable
        again = input("Play again? (y/n): ") #again variable
        print() # print statement
    print("Bye!") #print Bye

# if started as the main module, call the main function
if __name__ == "__main__": #main function
    main() #main

