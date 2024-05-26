#Addinf whitespace to strings with tabs or newline.

# prints string to the current line.
print('python')

# prints the string, but with a preceding whitespace using a tab.
print("\tpython")

# use \n for newline

print('Languages:\nPython\nJava\nJavascript')

# Stripping whitespcae

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip()) # will strip the whitespace off the string.

# for a permenant removal of the white space the string has to be associated with a new variable.

favorite_language = favorite_language.rstrip()
print(favorite_language)

