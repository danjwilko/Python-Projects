# Handling the FileNotFoundError Exception

from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')
# The read_text() is slightly different to what we did earlier on, the encoding argument is needed when your system's
# default encoding doesn't match the encoding of the file that's being read.
# Were going to try and read file that doesnt exist. the example will read a file but its not sved in the same directory
#  alice.py.


