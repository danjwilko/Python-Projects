import admin_details

john = admin_details.Admin('John', 'Smith', '21', 'user21js', 'Smith', 'Alaska')
john.describe_user()

john.privileges.show_privileges()

print("\nAdding privileges...")
john_privileges = ['can add post', 'can delete post', 'can ban user']
john.privileges.privileges = john_privileges
john.privileges.show_privileges()