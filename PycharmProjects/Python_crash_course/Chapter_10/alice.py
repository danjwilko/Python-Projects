# Handling the FileNotFoundError Exception

# from pathlib import Path
#
# path = Path('alice.txt')
# contents = path.read_text(encoding='utf-8')

# The read_text() is slightly different to what we did earlier on, the encoding argument is needed when your system's
# default encoding doesn't match the encoding of the file that's being read.
# Were going to try and read file that doesnt exist. the example will read a file but its not sved in the same directory
#  alice.py.

# running the program gives traceback which is quite long:

# Traceback (most recent call last):
#   File "/home/daniel/Documents/Github files/Python-Projects/PycharmProjects/Python_crash_course/Chapter_10/alice.py",
#   line 6, in <module>
#     contents = path.read_text(encoding='utf-8')
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/lib64/python3.12/pathlib.py", line 1027, in read_text
#     with self.open(mode='r', encoding=encoding, errors=errors) as f:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/lib64/python3.12/pathlib.py", line 1013, in open
#     return io.open(self, mode, buffering, encoding, errors, newline)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

# To handle the error being raised the try block will begin with the line that was identified as problematic
# in the traceback. In our example this is the line that conations the read_text().

from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

