# it is a brief Tour of the Standard Library


import os

print(os.getcwd())
print(os.system("ping baidu.com"))
print("666")

print(os.system("ping google.com"))
print("OMG I'm in china T_T")

print(dir(os))

import glob


print(glob.glob("lk_02*.py"))

s = "This is an String".replace("an", "a")
print(s)


