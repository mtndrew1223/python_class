#Name: Andrew Young
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section number
#Professor: Bartholomew
#Date:
#Project #: MO4_P1

print ("Andrew Young's Letter Grade Converter")
print ()

choice = 'y'
while choice.lower() == "y":
    number = int(input("Enter Numerical Grade: "))
    
    if number >= 94:
        letter = "A"
    elif number >= 90 :
        letter = "A-"
    elif number >= 87:
        letter = "B+"
    elif number >= 84:
        letter = "B"
    elif number >= 80:
        letter = "B-"
    elif number >= 77:
        letter = "C+"
    elif number >= 74:
        letter = "C"
    elif number >= 70:
        letter = "C-"
    elif number >= 67:
        letter = "D+"
    elif number >= 64:
        letter = "D"
    elif number >= 60:
        letter = "D-"
    elif number < 63:
        letter = "E"

    print("Letter Grade: " + letter)


    choice = input("Continue? (y/n): ")

print("Bye!")
