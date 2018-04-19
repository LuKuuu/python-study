# python IO

# f = open("diary.txt", "w")
f = open("diary.txt", "r")



print(f.read())

f.close()

# usage of with (similar as try...catch...finally)
"""with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
"""

f2 = open("diary.txt", "r")

while True:
    story = f2.readline()
    if story != "":
        print(story, end=" ")
    else:
        print("-" * 20)
        print("That's the end")
        print("")
        break

f2.close()


f3 = open("diary.txt", "r")
for line in f3:
    print(line, end=" ")

f3.close()

"""
f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from 
the beginning of the file when in binary mode and an opaque number when in text mode."""

f4 = open("diary.txt", "a")
f4.write("this is an appendix")
f4.close()
