# test of raise()
try:
    i = 1/1
    print("I think it's right", end="\n")
except ZeroDivisionError:
    print("there is some error here")
    raise  # if there is no error, nothing will be shown

try:
    j = 1/0
except ZeroDivisionError:
    print("something went wrong")
    # nothing is shown in the terminal, it looks fine if there is no print()

try:
    k = 1/0
except ZeroDivisionError:
    print("something went wrong")
    raise  # it makes you realize what went wrong






