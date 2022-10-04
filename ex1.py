'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


'''
print("i bet i can guess what year you will be 100")
Num1 = int(input("how old are you?"))
Num2 = 2022
Num3 = 100
print("you will be 100 in...")
print(Num2 - Num1 + Num3)

copies = int(input("how many copies do you want"))
