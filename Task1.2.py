import sys
data = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47, 35, 35, 48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3, 27, 6, 22, 9, 20, 18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12, 0, 22, 28, 47, 4, 5, 1, 11, 21, 1, 44, 24, 42, 42, 41, 14, 24]
less_40 = True
a = []
for elem in range(len(data)):
    if data[elem]<=40:
        less40.append(data[elem])
for elem in range(len(less40)):
    less_40 = True
    for elem2 in range(len(less40)):
        if less40[elem] == less40[elem2] and elem != elem2:
            less_40 = False
            break
    if less_40:
        a.append(less40[elem])
for elem in range(41):
    less_40 = True
    for elem2 in range(len(a)):
        if a[elem2] == elem:
            less_40 = False
            break
    if less_40: print(elem, end=' ')