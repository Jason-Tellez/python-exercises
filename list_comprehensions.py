fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]
(f.upper() for f in fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [f.capitalize() for f in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
#Hint: You'll need a way to check if something is a vowel.
vowels = ['a', 'e', 'i', 'o', 'u']
fruits_with_more_than_two_vowels = [f for f in fruits if len([v for v in f if v in vowels]) > 2]
fruits_with_more_than_two_vowels

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
vowels = ['a', 'e', 'i', 'o', 'u']
fruits_with_more_than_two_vowels = [f for f in fruits if len([v for v in f if v in vowels]) == 2]
fruits_with_more_than_two_vowels

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_chars = [f for f in fruits if len(f) >= 5]
fruits_with_more_than_five_chars

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_exactly_five_chars = [f for f in fruits if len(f) == 5]
fruits_with_exactly_five_chars

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_chars = [f for f in fruits if len(f) < 5]
fruits_with_less_than_five_chars

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_chars = [len(f) for f in fruits]
number_of_chars

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [f for f in fruits if f.find('a') > 0]
fruits_with_letter_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [num for num in numbers if num % 2 == 1]
odd_numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [num for num in numbers if num > 0]
positive_numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [num for num in numbers if num < 0]
negative_numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more_numerals = [n for n in numbers if len(str(n)) >= 2]
two_or_more_numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [n * n for n in numbers]
numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n % 2 == 1]
odd_negative_numbers

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [n + 5 for n in numbers]
numbers_plus_5

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
primes = [n for n in numbers if all(n % i != 0 for i in range(2, int(n / 2 + 1))) and n != 0] # the all function eliminates any integer where "i" divides n where i ranges from 2 to "n / 2" or half of n
primes