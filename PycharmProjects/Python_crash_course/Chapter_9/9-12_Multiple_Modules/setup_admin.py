from admin import Admin

john = Admin('John', 'Smith', '21', 'user21js', 'Smith', 'Alaska')
john.describe_user()

john.privileges.show_privileges()

print("\nAdding privileges...")
john_privileges = ['can add post',
                   'can delete post',
                   'can ban user'
                   ]
john.privileges.privileges = john_privileges
print(f" The admin {john.username} has these privileges: ")
john.privileges.show_privileges()
