# Writing to a file
# One of the simpliest ways of saving data is to write it to a file. when text is written to a file, the output
# will be available after you close the terminal containing your programs output.

# Writing to an empty file.
# To write to a file we need to call open() with a second argument telling python that you want to write to a file.



filename = 'programming.text'

with open(filename, 'w') as file:
    file.write('I love programming')
