row = []
for i in range(0, 9):
    row.append(0)

column = []
for j in range(0, 9):
    column.append(row)

print(column)

for i in range(0, 9):
    for j in range(0, 9):
        prompt = "please input the number of (" + str(i) + "," + str(j) + ")."
        print(prompt)


def cube(x): return x*x*x


list2 = map(cube, range(1, 11))

for i in list2:
    print(i)


def even(x): return x%2 == 0


list3 = filter(even, range(1, 1000))

for j in list3:
    print(j)


def product(sqe):
    def multply(x, y):
        return x*y
    from functools import reduce
    return reduce(multply, sqe, 1)


print(product(range(1, 5)))

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)
print(type(squares))
squares.append([x**2 for x in range(11)])

print(squares)
print(type(squares))


# usage of set
girls_i_love = ["Kun Qian", "my mum"]
loved_girl = set(girls_i_love)
print("Kenna" in loved_girl)
girls_i_love.append("my wife")

loved_girl = set(girls_i_love)
print("my wife" in loved_girl)

# usage of dictionary
qq_num = dict()
qq_num["Chengyang"] = 1240291449
qq_num["Kun"] = 409036894

print(qq_num)

unknown_list = dict(sape=4139, guido=4127, jack=4098)


# usage of enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['Kun Qian', 'watching movie', 'yellow']

for q, a in zip(questions, answers):
    print('what is your {0}?   It is {1}.'.format(q, a))


# usage of sort
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

""""""
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
""""""

