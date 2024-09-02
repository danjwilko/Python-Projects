with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
# Rstrip removes the blank line left by read() when it reaches the end of the file.
print(contents.rstrip())

# File paths.

# Sometimes we may need to use a relative file path. A relative file path, tells Python to look for a given location
# relative to the directory where the currently running program file is stored.
#
# with open('text_files/filename.txt') as file_object:

# Note: Windows systems use a backslash (\) instead of a forward slash (/) when displaying file paths, but you can
# still use forward slashes in your code.

# We can also tell Python exactly where the file is on a computer regardless of where the program is that's being
# executed is stored. This is called an absolute file path. You can use an absolute file path if the relative path
# doesn't work.

# Absolute paths are usually longer than relative paths so its helpful to assign them to variable and then pass
# that variable to open()

# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# Note: If you try to use backslashes in a file path, youll get an error because the backslash is used to escape
# characters in strings. For example, in the path "C:\path\to\file.text", the \t is interpretted as a tab.
# If you need to use backslashes, you can escape each one in the path, like this: "C:\\path\\to\\file.txt".

# Reading Line by Line
# When reading a file often we will want to examine each line of the file.
# You can use a for loop on the file object to examine each line from a file at a time.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# on the output we get blank lines between the lines of text, thats because an invisible newline charater is at the
# end of each line in the text file. The print function adds its own new-line each time we call it so we end up with
# two newline characters at the end of each line: one from the file and one from the print(). Using rstrip() on each
# line in the print() call we can eliminate these extra blank lines.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# this is the output we get using this code:
# 3.14159265535
#    8979323846
#    2643383279



