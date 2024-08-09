import greet_function

usernames = ['hannah', 'ty', 'margot']

greet_function.greet_users(usernames)

from greet_function import greet_users
greet_users(usernames)

from greet_function import greet_users as greet

greet(usernames)

import greet_function as gu

gu.greet_users(usernames)

from greet_function import *
greet_function.greet_users(usernames)

