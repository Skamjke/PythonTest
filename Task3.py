import sys
data = []
for elem in range(1,101):
    data.append(elem)
for elem in range(len(data)):
    if data[elem] % 3 == 0 and data[elem] % 5 == 0:
        data[elem] = "FooBar"
    else:
        if data[elem] % 3 == 0:
            data[elem] = "Foo"
        else:
            if data[elem] % 5 == 0:
                data[elem] = "Bar"
    print(data[elem])

    
