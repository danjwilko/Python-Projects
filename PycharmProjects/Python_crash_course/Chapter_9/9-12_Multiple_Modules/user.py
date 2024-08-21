class User:
    def __init__(self, first_name, last_name, age, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.username = username
        self.login_attempts = 0
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location:{self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
