def divide_test(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Y shouldn't be zero")
    else:
        print(result)
    finally:
        print("finished")


divide_test(1, 2)

divide_test(1, 0)

with open("diary.txt") as f:  # the "with" can close the file after use
    for line in f:
        print(line, end="")

