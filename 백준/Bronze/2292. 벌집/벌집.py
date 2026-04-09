import sys

N = int(sys.stdin.readline())
floor = 1
end = 1

while end < N :
    end += 6 * floor
    floor += 1

sys.stdout.write(str(floor))