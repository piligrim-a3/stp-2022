log = open("access.log", "r")
arr = list()
while True:
    s = log.readline()
    s = s.split()
    if not s:
        break
    if len(arr) < 10:
        arr.append(s)
    else:
        m = arr.index(min(arr, key=lambda x: int(x[4])))
        arr[m] = max((arr[m], s), key=lambda x: int(x[4]))
print(*arr, sep='\n')