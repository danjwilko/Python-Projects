# Glossary

glossary = {'dictionary': 'Where items are stored as key-value pairs',
            'key-value pair': 'items in a dictionary have a key, which we can look up the value associated with.',
            'conditional tests': 'At the heart of every if statement is an expression that can be evaluated as True '
                                 'of False and is called a conditional test.',

            'boolean expression': 'boolean expression is just another name for a conditional test, a boolean value is '
                                  'either "True" or "False".',
            'range()': 'returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), '
                       'and stops before a specified number.',
            'keys()': 'Used to retrieve a keys from a dictionary.',
            'values()': 'Used to retrieve a values from a dictionary.',
            'sorted()': 'returns a sorted sequence of items.',
            'get()': 'returns the value of the item with the specified key.',
            'set': 'One of the methods used to store collections of data',


            }

for key, value in glossary.items():
    print(f'{key.title()}: {value}.')
