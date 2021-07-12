#You have rented some movies for your kids: 
        #The little mermaid (for 3 days), 
        #Brother Bear (for 5 days, they love it), 
        #and Hercules (1 day, you don't know yet if they're going to like it). 
#If price for a movie per day is 3 dollars, how much will you have to pay?
x = 3     #rental fee
lm = 3     #days little mermaid was kept
bb = 5     #days brother bear was kept
he = 1     #days hercules was kept
total = x * (lm + bb +he)
print(total)

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
#they pay you a different rate per hour. 
#Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
#How much will you receive in payment for this week? 
#You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
gg = 400     #google rate
am = 380     #amazon rate
fb = 350     #facebook rate
gh = 6     #google hours
fh = 10     #facebook hours
ah = 4     #amazon hours
pay_per_co = [gg * gh, am * ah, fb * fh]
tot_pay = sum(pay_per_co)
print(tot_pay)

#A student can be enrolled to a class only if the class is not full 
#and the class schedule does not conflict with her current schedule.
enroll_status = class_not_full and no_conflicting_class

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
#Premium members do not need to buy a specific amount of products.
valid_offer = (more_than_2_items and offer_expiration) or is_premium_mem

#Create a variable that holds a boolean value for each of the following conditions:
    #the password must be at least 5 characters
    #the username must be no more than 20 characters
    #the password must not be the same as the username
    #bonus neither the username or password can start or end with whitespace
username = 'codeup'
password = 'notastrongpassword'
char_min = len(password) >= 5
char_max = len(username) <= 20
pass_user_match = username != password
no_whitespace = (not username.startswith(' ') and not username.endswith(' ') and not password.startswith(' ') and not password.endswith(' '))
no_whitespace

