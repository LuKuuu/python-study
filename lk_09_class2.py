import sys

# print(dir(sys))


class Cat:
    pass


qk = Cat()
qk.First_Name = "Kun"
qk.Last_name = "Qian"

print(qk.First_Name)

for num in [1, 2, 3]:
    print(num)

name = "Qian"
for letters in name:
    print(letters)

numbers = {"one": 1, "two": 2, "three": 3}
for key in numbers:
    print(key)

it = iter(name)
print(it)
for i in range(4):
    print(next(it))


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)


def double(item):
    item = item + item
    item


print(double(9))
