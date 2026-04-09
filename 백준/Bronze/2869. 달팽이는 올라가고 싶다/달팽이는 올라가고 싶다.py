import sys

A, B, V = map(int, sys.stdin.readline().split())

if (V - A) % (A - B) == 0:
    sys.stdout.write(str((V - A) // (A - B) + 1))
else:
    sys.stdout.write(str((V - A) // (A - B) + 2))
