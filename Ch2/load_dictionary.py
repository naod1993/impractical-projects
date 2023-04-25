""""
Arguments:
- text file name (and discovery path, if needed)

Exceptions:
- IOError if filename not found

Retruns:
- A list of all words in a text file in lower case
"""

import sys

def load_file(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}.Terminating program.".format(e,file),file=sys.stderr)
    sys.exit(1)


