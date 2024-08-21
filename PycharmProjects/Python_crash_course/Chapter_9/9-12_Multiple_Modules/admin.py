from user import User


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
