# This program uses a while loop to allow users to add multiple blogs.

posting_active = True;

blogs = []

print("\nWelcome to Blogs of The Week! Share your thoughts!")

while posting_active:
    
    answer = input("\nWould you like to post a blog today? 'yes' or 'no' ")
    
    if answer == 'no':
        posting_active = False
    else:
        name = input("Please enter your name: ")
        title = input("Title of your blog: ")
        text = input("Please enter text for your blog: ")

        blogs.append({'user' : name, 'title' : title, 'body': text})

print("\n----Blogs of The Week---")

if len(blogs) == 0:
    print("\nSorry! There are currently no blogs available!")
else:
    for post in blogs:
        print("--------")
        print(f"\n{post['title'].title()} by {post['user'].title()}")
        print(f"\n{post['body']}\n")

print("\nThank you for using this app! =)\n")
    

    
