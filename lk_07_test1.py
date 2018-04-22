# usage of str and repr

hello = "hello\n" + " !"
print(hello)
print(str(hello))
print(repr(hello))

import math
for r in range(10):
    if r == 0:
        print(print(str("r").rjust(5), str("2 * r * 3.14").rjust(5)))  # right-justifies a string in a field
    else:
        s = str(2 * r * math.pi)
        print(s.zfill(5))  # useless for pi
        print(str(r).rjust(5), s.zfill(5))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

print('The value of PI is approximately {0:.5f}.'.format(math.pi))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:5}'.format(name, phone))



