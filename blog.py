# This module is for creating and displaying blogs.

def create_blog(blogs_list, name, blog_title, blog_body):
    """Create a blog post"""
    
    blogs_list.append({'author' : name, 'blog' : {'title' : blog_title, 'body': blog_body} })

def print_blogs(blogs):
    """Displays the collection of blogs"""
    
    for post in blogs:
        print('\n------')
        print(f"\n{post['blog']['title'].title()} by {post['author']}")
        print(f"\n{post['blog']['body']}\n")
        print('------\n')