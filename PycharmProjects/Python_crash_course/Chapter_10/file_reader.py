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

# Note: windows systems use a backslash (\) instead of a forward slash (/) when displaying file paths, but you can
# still use forward slashes in your code.

