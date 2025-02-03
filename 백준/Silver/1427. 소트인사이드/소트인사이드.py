n = str(input())
ex = []

for i in n :
    ex.append(int(i))

ex.sort()

for i in range(len(ex) - 1, -1, -1) :
    print(ex[i], end = "")