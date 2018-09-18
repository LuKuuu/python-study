def scopes_test():
    """a test of the scopes global, local, and nonlocal"""
    def global_test():
        global i
        i = 1

    def local_test():
        j = 2

    def nonlocal_test():
        nonlocal kkkk
        kkkk = 3


scopes_test()

"""I stilllll cannot understand this one"""

