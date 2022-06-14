log = open("access.log", "r")
arr = list()
while True:
    '''Построчное считываение файла'''
    s = log.readline()
    s = s.split()
    '''Если строка пустая'''
    if not s:
        break
    '''если массив ещё меньше 10, добавляем всё подряд'''
    if len(arr) < 10:
        arr.append(s)
    else:
        '''Сравниваем с минимальным элементом текущий, из читаемой строки'''
        m = arr.index(min(arr, key=lambda x: int(x[4])))
        arr[m] = max((arr[m], s), key=lambda x: int(x[4]))
'''сортировка по убыванию'''
arr = sorted(arr, key=lambda x: -int(x[4]))
'''Запись в файл'''
f = open('out.txt', 'w')
for s in arr:
    f.write(" ".join(s) + '\n')