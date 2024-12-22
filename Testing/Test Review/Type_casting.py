#typecasting

value_1 = 10 #an integer

value_2 = '10' #a string: the difference bewtween str and float is how we do math

value_3 = 10.0 #float (floating decimal point)

print("number" + value_1)  #this will not work, because there is an integer in there.
#in the above code, there is a str and an integer, which will not work. You have to typecast it and make the integer into a string
print("number" + str(value_1))

number = input("Enter Number: ") #aynthing you put in here will be a str
number = int(input("Enter Number: ")) #This will make it an integer
#However, you can not put letter such as 'ten' in the above code, or decimals


