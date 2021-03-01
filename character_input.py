
"""""
Exercise 1
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
name = input('Hello Stranger! Tell me your name?')
print('Hello ' + name + "!")
age = input('How old are you?')
years = 100 - int(age)
print('You will be a 100 in ' + str(years) + " years")

"""""
Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""
number = input("Give me a random number")
print(int(number) * ("You will be a 100 in " + str(years) + " years \n"))