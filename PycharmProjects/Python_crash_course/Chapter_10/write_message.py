# Writing to a file
# One of the simpliest ways of saving data is to write it to a file. when text is written to a file, the output
# will be available after you close the terminal containing your programs output.

# Writing to an empty file.
# To write to a file we need to call open() with a second argument telling python that you want to write to a file.


filename = 'programming.txt'

with open(filename, 'w') as file:
    file.write('I love programming')

# Note: Python can only write strings to a text file.If we want to store numerical data we have to convert the data
# a string format first using str().

# Writing multiple lines

# The write() function doesnt add any newlines to the text you write. So if we write more than one line without
# including a newline character the file may not look how we want it too.

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming')
    file_object.write('I love creating games')

# We get the following in the text file: I love programmingI love creating games

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming. \n')
    file_object.write('I love creating games. \n')

# We now get the following:
# I love programming.
# I love creating games.

# Appending to a file.

# If we want to add content to a file instead of writing over any existing content, we can use the append mode 'a'.
# When a file is opened in append-mode, Python doesn't erase the contents of the file before returning the file object.
# Any lines we write are written to the end of the file.

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets. \n')
    file_object.write('I love creating apps that can run in the browser. \n')
