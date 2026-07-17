# This program is continuation of the blogging example from before

from app_functions import login
from app_functions import logout
from app_functions import add_user
from account import Account

logged_in = login()
exit_message = "Thanks for stopping by! =)"
success_message = "Thank you! Account has been successfully created"

accounts = []

response = input("Do you have an account: 'y' or 'n': ")

if response == "n":
    decision = input("Would you like to sign up? 'y' or 'n': ")
    if decision == "n":
        print(exit_message)
    else:
        username = input("Please create a username: ")
        password = input("Please create a password: ")
        email = input("Please provide a vailid email: ")

        add_user(accounts, Account(username, password, email))

        if accounts:
            logged_in = login()
            print(success_message)

while logged_in:
    choice = input(f"Welcome {accounts[0].username}! What would you like to post a blog? ")
    
    if choice == 'y':
        # create a new blog and attach to the account
        print("This is me creating a blog")
    else:
        logged_in = logout()
