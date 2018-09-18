class FirstPythonClass:
    """here are some discription"""

    def __init__(self):
        the_number_inside = 888

    i = 666

    def first_function(self, i, s):
        t = 0
        while t < 5:
            print(s)
            t = t + 1


test = FirstPythonClass()
test.first_function(5, "print this five times")

print(test.__init__())
