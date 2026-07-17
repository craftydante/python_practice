# This program builds on the while program by including functons.

from blog import create_blog
from blog import print_blogs
from blog import is_user
from blog import add_blog


posting_active = True;

blog_accounts = []

print("\nWelcome to Blogs of The Week! Share your thoughts!")

while posting_active:
    
    answer = input("\nWould you like to post a blog today? 'yes' or 'no': ")

    if answer != 'yes' and answer != 'no':
        print("The answer you've enter is invalid! Please enter 'yes' or 'no'.")
        continue
    
    if answer == 'no':
        posting_active = False
    else:
        name = input("Please enter your name: ")
        title = input("Title of your blog: ")
        text = input("Please enter text for your blog: ")

        if is_user(blog_accounts, name):
            add_blog(blog_accounts, name, title, text)
        else:
            create_blog(blog_accounts, name, title, text)

print("\n----Blogs of The Week---")

if len(blog_accounts) == 0:
    print("\nSorry! There are currently no blogs available!")
else:
    print_blogs(blog_accounts)
        
print("\nThank you for using this app! =)\n")

print(blog_accounts)
    

    
