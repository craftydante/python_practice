# This program builds on top of the previous blogging example

from account import Account
posting_active = True;

accounts = []

print("\nWelcome to BlogMe! Share your thoughts!")

while posting_active:
    
    answer = input("\nWhat would you like to do? (S)Sign Up, (L)Login, or (Q)Quit ?: ")
    
    if answer == 'q' or answer == 'Q':
        posting_active = False
    elif answer == 'l' or answer == 'L':
        print("logging in user!")
        break
    else:
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        email = input("Please enter a valid email: ")
        
        accounts.append(Account(username=username, email=email, password=password))
    break
print(accounts)


print("\nThank you for using this app! =)\n")
    

# Goals:
# Figure out how to login a user 
# Figure out how to select the current instane of an object in a list
# Figure out how to search through different objects 
