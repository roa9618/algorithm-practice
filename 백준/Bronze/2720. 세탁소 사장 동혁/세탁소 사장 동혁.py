import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T) :
    N = int(sys.stdin.readline().rstrip())
    result = []

    for j in [25, 10, 5, 1] :
        result.append(str(N // j))
        N %= j
        
    sys.stdout.write(' '.join(result) + '\n')