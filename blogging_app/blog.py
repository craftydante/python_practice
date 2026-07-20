# This module is for creating and displaying blogs.

def create_blog(accounts, name, title, body):
    """Create a blog post"""
    
    accounts.append({ name : [{'title': title, 'body' : body}]})

def is_user(accounts, name):
    for account in accounts:
        if name in account:
            return True

def add_blog(accounts, name, title, body):
    """Add blog to existing user"""
    for account in accounts:
        if name in account:
            account[name].append({'title' : title, 'body': body})

def print_blogs(accounts):
    """Displays the collection of blogs"""
    
    for account in accounts:
        for author, blogs in account.items():
            for blog in blogs:
                print('\n------')
                print(f"\n{blog['title'].title()} by {author}")
                print(f"\n{blog['body']}")
                print("\n------\n")
