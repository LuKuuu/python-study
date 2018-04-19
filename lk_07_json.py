# usage of json (JavaScript Object Notation)
import json
f = open("json_file1", "w")

# json.dump("hello, json!", f)
# json.dump(1, f)

print(json.load(f))

"""
There are still something cannot be understand in this part, such as how to read information from json file
"""