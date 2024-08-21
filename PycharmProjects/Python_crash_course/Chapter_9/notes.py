# Defining Attributes and Methods for the child class.
    # Once we have a child class that inherits from a parent class, you can add any attributes and methods necessary to
    # differentiate the child class from the parent class.

# There's no limit to how much we specialise the ElectricCar class. You can add as many attributes and methods
# as we need to model an electric car to whatever degree of accuracy we need.
# An attribute or method that could belong to any car, rather than one that's specific to an electric car, should be
# added to the Car class instead of the ElectricCar class.

# Overriding Methods from the parent class.

# You can override any method from the parent class that doesn't fit what your trying to model with the child class.
# To do this, we define a method in the child class with the same name as the method you want to override in the parent
# class.
# Python will disregard the parent class method and only pay attention to the method you defined in the child class.

# Instances as Attributes.

# When modelling something from the real world in code, you may find that you're adding more and more details to
# a class.
# You'll find that you have a growing list of attributes and methods, and the files are becoming lengthy.
# We might recognise at this point that part of one class can be written as a separate class.
# We have modified the ElectricCar class above and moved the battery details to its own class.

# Modelling Real-World Objects.
# As we begin to model more complicated things like electric cars, you'll wrestle with interesting questions.
# Is the range of an electric car a property of the battery or the car?
# If were only describing one car, it's probably fine to maintain the association of the method get_range() with the
# battery class.
# But if were describing an entire manufacturer's entire line of cars, we probably want to move get_range() to the
# ElectricCar class.

# Importing the entire module.
# We can also import the entire module and access the classes we need using dot notation.

# We can also import every class from module using the following syntax:
# from module_name import *
# however, this method is not recommended for two reasons:
# 1. It's helpful to be able to read import statements and get a clear sense of what classes the program is utilizing.
# 2. It can also create confusion with names in the file if you accidentally import a class with the same name as
# something in the program, you can create errors that are hard to diagnose.

# Importing a Module into a module.

# Sometimes you'll want to spead out your classes across several modules to keep any one file from getting to large.
# When you store your classes in several modules, you may find that a class in one module may rely on a class in another
# module, when this happens you can import the required class into the first module.
