import sys

N, B = map(int, sys.stdin.readline().split())
result = []

while N > 0 :
    if N % B < 10 :
        result.append(str(N % B))
    else :
        result.append(chr(N % B - 10 + ord('A')))

    N //= B
    
sys.stdout.write(''.join(result[::-1]))