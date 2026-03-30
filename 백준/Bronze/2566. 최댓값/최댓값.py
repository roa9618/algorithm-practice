import sys

arr = []
max_num = -1
x = -1
y = -1

for i in range(9) :
    inp = list(map(int, sys.stdin.readline().split()))
    arr.append(inp)

for i in range(9) :
    for j in range(9) :
        if arr[i][j] > max_num :
            max_num = arr[i][j]
            x = i
            y = j

sys.stdout.write(str(max_num) + "\n")
sys.stdout.write(str(x + 1) + " " + str(y + 1))