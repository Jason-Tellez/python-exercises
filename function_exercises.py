# 1. Define a function nmed is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
#the function named is_two takes in a single parameter named value that can be a string or integer
def is_two(value):      
    #checks if the input given is either the integer 2 or the string '2'
    if value == 2 or str(value) == '2':
        #returns true if either conditions are met
        return True
    #otherwise it returns false
    else:
        return False

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
#the function named is_vowel has a parameter called letter
def is_vowel(letter):
    #converts the string to lower case to check if the string is contained in the string of vowels
    if letter.lower() in 'aeiou':
        #if the input is a vowel, the function returns true
        return True
    #if the input is not a vowel, the string returns false
    else:
        return False

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
#function named is_consonant that takes a parameter called letter, that is a string
def is_consonant(letter):
    #calls the is_vowel function to test whether input is vowel
    if is_vowel(letter) == True:
        #if is_vowel is true, is_consonant is false
        return False
    #vice versa
    else:
        return False

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_letter(word):
    if word[0] not in 'aeiou':
        return word.capitalize()
    else:
        return word

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
#function called calculate tip that takes two parameters that are numeric data types
def calculate_tip(tip_per, balance):
    #variable named total acts as equation to combine both tip and balance
    total  = balance * (tip_per + 1)
    return total

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
##function named apply_discount takes two parameters, both are numeric datatypes
def apply_discount(price, disc_per):
    #the total variable acts as the equation to find price of item minus the discount
    total = price * (1- disc_per)
    return total

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
#function named handle_comas that takes a parameter named num_str which is a string
def handle_commas(num_str):
    #the .replace() function removes any commas from the string
    result = num_str.replace(',', '')
    return result

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
#function named get_letter_grade that takes in a parameter named number that is an integer
def get_letter_grade(number):
    #if condition to return A if number is within range of A
    if number in range(90,101):
        return 'A'
    #if condition to return B if number is within range of A
    if number in range(80,90):
        return 'B'
    #if condition to return C if number is within range of A
    if number in range(70,80):
        return 'C'
    #if condition to return D if number is within range of A
    if number in range(60,70):
        return 'D'
    #else condition prints F if no other conditions are met
    else:
        return 'F'

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
#this remove_vowels function takes in one parameter called word, a string, that removes vowels
def remove_vowels(word):
    #for loop to iterate through characters in word
    for letter in word:
        #if condition that determines if any letter in word is a vowel
        if letter in "aeiou":
            #if any letter in word is a vowel, it will be removed from word
            word = word.replace(letter, '')
    return word

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    #anything that is not a valid python identifier should be removed
    #leading and trailing whitespace should be removed
    #everything should be lowercase
    #spaces should be replaced with underscores
#function named normalize_name that takes in a paramenter called name, a string, and returns name with only valid identifiers
def normalize_name(name):
    #for loop to iterate through each character in name
    for symbol in name:
        #if condition to determine if any character is not a valid identifier
        if symbol not in "abcdefghijklmnopqrstuvwxyz1234567890_":
            #changes all letters to lower case
            name = name.lower()
            #removes any invalid identifier
            name = name.replace(symbol, '')
            #removes any leading or trailing whitespace
            name = name.strip()
            #replace whitespaces with an underscore
            name = name.replace(' ', '_')
    return name

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#function called cummulative sum that takes one parameter called num, a list of integers, and returns a list of the sume of each element and its preceeding elements
def cumulative_sum(num):
    #for loop that iterates from the beginning of the list to the last element
    for n in range(num[0], len(num)):
        #the addition assignment operator adds the current value which is being iterated and the previous value in the list
        num[n] += num[n-1]
    return(num)