#1. Conditional Basics
#a. prompt the user for a day of the week, print out whether the day is Monday or not
user_input = input("What day is today?")
if user_input == "Monday":
    print("I hate Mondays!")
else:
    print('Have a good day!')

#b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("What day is today?")
if day == "Monday" or "Tuesday" or "Wednesday" or "Thursday":
    print("It's a weekday.")
elif day == "Friday" or "Saturday" or "Sunday":
    print("It's the weekend!")

#c. create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hours_a_week = 45
hourly_rate = 7.25
paycheck = hourly_rate * hours_a_week
if hours_a_week > 40:
    overtime = (hours_a_week - 40) * (hourly_rate * 1.5)
    paycheck = 40 * hourly_rate + overtime 
    print("Your weekly pay is", paycheck)
else:
    print("Your weekly pay is", paycheck)


#2. Loop Basics
#a. While
#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i <= 100 and i >= -10:
    print(i)
    i -= 5
#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
i = 2
while i < 1000000:
    print(i)
    i = i ** 2
#Write a loop that counts from 100 to 5 in increments of 5.
i = 100
while i <= 100 and i >= 5:
    print(i)
    i -= 5

#b. #For Loops
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
num = input("Gimme a number!")
num = int(num)
for m in range(1, 11):
    print(num, 'x', m, '=', num * m)
#Create a for loop that uses print to create the output shown below.
mult = 1, 2, 3, 4, 5, 6, 7, 8, 9
product = 0
for m in mult:
    product = m * [m]
    print(product)

#c break and continue
#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
#(Hint: use the isdigit method on strings to determine this). 
#Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
number = input("Pick an odd number between 1 and 50.")
while number.isdigit() == False or int(number) % 2 == 0:
    print(f"{number} is not a valid entry!")
    number = input("Please pick a valid odd number between 1 and 50.")
    i_quit = input("If you want to be a quitter, type 'Y'")
    if i_quit == "Y" or i_quit == "y":
        break
    else:
        number = input("Please pick a valid odd number between 1 and 50.")
        continue
print("Number to skip is:", number)
for i in range(1,51):
    if i % 2 == 1 and i != int(number):
        print("Here is an odd number:", i)
    if i == int(number):
        print("Yikes! Skipping number:", number)

#d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
positive_number = input("Pick a positive integer.")
while positive_number.isdigit() == False or int(positive_number) <= 0 or int(positive_number) % 1 != 0:
    print(f"{positive_number} is not a valid input.")
    try_again = input("Continue? Y/N?")
    if try_again == "N" or try_again == "n":
        print("okie dokie")
        break
    else:
        positive_number = input("Pick a positive integer.")
        continue
for num in range(0,int(positive_number) + 1):
    print(num)

#e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
positive_int = input("Pick a positive integer.")
while positive_int.isdigit() == False or int(positive_int) <= 0 or int(positive_int) % 1 != 0:
    print(f"{positive_int} is not a valid input.")
    try_again = input("Continue? Y/N?")
    if try_again == "N" or try_again == "n":
        print("okie dokie")
        break
    else:
        positive_int = input("Pick a positive integer.")
        continue
for num in range(int(positive_int), 0, -1):
    print(num)

#3. Fizzbuzz
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".
for int in range(1, 100 +1):
    if int % 3 == 0 and int % 5 != 0:
        print("Fizz")
    elif int % 5 == 0 and int % 3 != 0:
        print("Buzz")
    elif int % 5 == 0 and int % 3 == 0:
        print("FizzBuzz")
    else:
        print(int)

#4. Display a table of powers.
#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.
integer = int(input("Gimme any integer to get a neat table."))
header = " {:^4} "              #header, line, and body variable create and space the table when printed
body = " {:^6} "
body2 = " {:^7} "
line = " {:^6} "
line2 = " {:^7} "
print(header.format('number'), "|", header.format('squared'), "|", header.format('cubed'))
print(line.format('------'), "|", line2.format('-------'), "|", line.format('-----'))
confirmation = input("If you want to quit, type 'N'. Else, type anything!")
while int(integer) == True:
    if confirmation == "N" or confirmation == "n":
        print("okie dokie")
        break
    else:
        print("Here you go!")
        continue
if integer >= 1:
    for x in range(1, integer + 1):
        print(body.format(x), "|", body2.format(x ** 2), "|", body.format(x ** 3))
if integer < 1:
    for x in range(1, integer - 1, -1):
        print(body.format(x), "|", body2.format(x ** 2), "|", body.format(x ** 3))