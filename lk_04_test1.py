a = list(range(10))
print(a)
print(type(a))


def f(b, li=list()):  # it is the same if we write li=[]
    li.append(b)
    return li


print(f(1))
print(f(2))
print(f(3))


def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheese_shop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def my_function():
    """Do nothing, but document it.

     No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)

