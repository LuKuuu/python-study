# this is a test related to error
"""
8.1. Syntax Errors
8.2. Exceptions


"""

a = 1
b = "1"
c = str(a) + b
d = int(c)
e = d/11
print(e)

# 8.3 handle error
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# example of try...except
import sys

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except Exception:
    print("Unexpected error:", sys.exc_info()[0])
    raise



