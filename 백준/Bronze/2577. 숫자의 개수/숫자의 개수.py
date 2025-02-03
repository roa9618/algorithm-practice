save = []

a = int(input())
b = int(input())
c = int(input())

total = str(a * b * c)

for i in total :
    save.append(i)

for j in range(10) :
    print(save.count(str(j)))