print('Задание 1')
log = open("access.log", "r")
arr = list()
while True:
    s = log.readline()
    if not s:
        break
    if len(arr) < 10:
        arr.append(s.split())
print(*arr, sep='\n')