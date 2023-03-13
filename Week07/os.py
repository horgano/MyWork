

import os

FILENAME = "messing_with_files"

if os.path.exists (FILENAME):
    with open (FILENAME, "r") as f:
        for line in f:
            print (line, end="")
else:
    print (FILENAME, "does not exist")

#os.remove("data2.txt")
# to delete