import sys

result = 0
n, b = sys.stdin.readline().split()

for i in range(len(n)) :
    if n[i].isdigit() :
        result += int(n[i]) * int(b) ** (len(n) - i - 1)
    else :
        result += (ord(n[i]) - ord('A') + 10) * int(b) ** (len(n) - i - 1)

sys.stdout.write(f"{result} \n")