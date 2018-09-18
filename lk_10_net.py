from urllib.request import urlopen

f = open("data.txt", "w")

with urlopen("https://cn.bing.com/") as responce:
    for line in responce:
        line = line.decode('utf-8')
        if "href" in line:
            print(line)

g