class User:
    def __init__(self, first_name, last_name, age, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} \n\tUsername: {self.username} \n\tEmail: {self.email} \n\tLocation:{self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")


user1 = User("John", "Doe", '23', 'JD23', '<John@gmail.com>', 'Lincoln')
user1.greet_user()
user1.describe_user()

user2 = User("Daniel", "smith", '45', 'Dans80', 'dsmith80@gmail.com', 'york')
user2.greet_user()
user2.describe_user()
