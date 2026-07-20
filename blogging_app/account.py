class Account:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.blogs = []

    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_blogs(self):
        return self.blogs
    
    def update_email(self, new_email):
        self.email = new_email
    
    def update_username(self, new_username):
        self.username = new_username

    def update_password(self, new_password):
        self.password = new_password