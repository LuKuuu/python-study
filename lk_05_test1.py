list =[1, 4, 88, 27, 19]
print(list)
list.append(55)
print(list)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.count("Eric"))

# There are three built-in functions that are very useful when used with lists: filter(), map(), and reduce()


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
# The following list comprehension will transpose rows and columns:

print([[row[i] for row in matrix] for i in range(4)])
