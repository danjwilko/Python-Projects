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


class Admin(User):
    def __init__(self, first_name, last_name, age, username, email, location):
        super().__init__(first_name, last_name, age, username, email, location)

        self.privileges = Privileges()


class Privileges:

    def __init__(self, privileges=None):
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t-{privilege}")
        else:
            print("No Privileges")


john = Admin('John', 'Smith', '21', 'user21js', 'Smith', 'Alaska')
john.describe_user()

john.privileges.show_privileges()

print("\nAdding privileges...")
john_privileges = ['can add post', 'can delete post', 'can ban user']
john.privileges.privileges = john_privileges
john.privileges.show_privileges()

