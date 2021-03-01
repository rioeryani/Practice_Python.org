"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

"""

while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again..")

result = int(number) % 2

if result == 0:
    print ("The number you entered is an even number")
elif result != 0:
    print("The number you entered is an odd number")

"""
Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""
result = int(number) % 4

if result == 0:
    print ("The number is a multiple of four")
elif result != 0:
    print("The number is NOT a multiple of four")

print("This time I will need two sets of numbers")

while True:
    try:
        num = int(input("Give me your first number: "))
        break
    except ValueError:
        print("Oops, that is not a valid number. Try again..")
while True:
    try:
        check = int(input("Give me your second number: "))
        break
    except ValueError:
        print("Oops, that is not a valid number. Try again..")

result2 = int(num) % int(check)

if result2 == 0:
    print("The first number you picked divides evenly to your second number. ")
elif result2 !=0:
    print("Oops, the first number you picked do not divides evenly to your second number. ")
