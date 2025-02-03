a = []
max_num = 0

for i in range(9) :
    n = int(input())
    a.append(n)

for i in range(len(a)) :
    if a[i] > max_num :
        max_num = a[i]

print(max_num)
print(a.index(max_num) + 1)