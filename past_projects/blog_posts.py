# This program prints out blogs written by a user

accounts = [
    {
        'user' : 'Dante',
        'blogs' : [
            {
                'title' : 'A Walk To Remember',
                'body' : 'blog 1.'
            }
        ]
    },
    {
        'user' : 'Marco',
        'blogs': [
            {
                'title' : 'My First Business',
                'body' : 'Running a business is awesome!'
            }
        ]
    },
    {
        'user' : 'Luis',
        'blogs' : [
            {
                'title' : 'The Day I Got A Flat Tire',
                'body' : 'I got a flat tire!'
            }
        ]
    },
    {
        'user' : 'Arteaga',
        'blogs' : [
            {
                'title' : 'Silent Guy',
                'body' : 'I never speak so they call me silent!'
            }
        ]
    }
]

print('Popular Blogs of The Week!\n')

if accounts:
    for account in accounts:
        for blog in account['blogs']:
            print(f"{blog['title']}")
            print(f"by {account['user']}\n")
            print(f"{blog['body']}\n")

print("Come back tomorrow for our newest blogs!")