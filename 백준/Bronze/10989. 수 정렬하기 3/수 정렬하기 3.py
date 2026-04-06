import sys

N = int(sys.stdin.readline().rstrip())

count = [0] * 10001

for i in range(N) :
    num = int(sys.stdin.readline().rstrip())
    count[num] += 1

for i in range(10001) :
    if count[i] != 0 :
        for j in range(count[i]) :
            sys.stdout.write(str(i) + '\n')