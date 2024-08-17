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
        print(
            f"\n{self.first_name} {self.last_name} \n\tUsername: {self.username} \n\tEmail: {self.email} \n\tLocation:{self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, username, email, location):
        super().__init__(first_name, last_name, age, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print(f"Privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")


john = Admin('John', 'Smith', '21', 'user21js', 'Smith', 'Alaska')
john.privileges = 'can add post', 'can delete post', 'can ban user'
john.describe_user()
john.show_privileges()



