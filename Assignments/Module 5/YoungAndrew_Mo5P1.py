#Name: Andrew Young
#Class: (INFO 1200)
#Section: (001)
#Professor: Barty
#Date:
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.





def is_even(num):    #
    
    if int(num) % 2 == 0: 
        return True # code if it doesn't have a remainder
        
    else:
        return False



def main():
    print("Andrew's even or odd checker")
    print()
    my_num = input("Enter an integer: ")
    if is_even(my_num):
        print("This is an even number")
    else:
        print("This is an odd number")





if __name__ == "__main__":main()     
