
import re

def findIP(str):
    result = re.search(r'[0-2]\d{2}\.[0-2]\d{2}\.\d{,3}\.\d{,3}', str)
    return result.group()

def findInf(str):
    return re.sub(r'\s+', ' ', str).split(" ")[1]


if __name__ == '__main__':
    ipBook = dict()

    with open("access.log") as file:
        for line in file:
            ip = findIP(line)
            value = int(findInf(line))
            if ipBook.get(ip) is not None:
                value += ipBook[findIP(line)]
            ipBook[findIP(line)] = value

    sortedKeys = sorted(ipBook, key=ipBook.get, reverse=True)

    for x in range(10):
        print(ipBook[sortedKeys[x]], sortedKeys[x])
