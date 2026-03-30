import sys

n = sys.stdin.readline().strip()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia :
    n = n.replace(i, '*')

sys.stdout.write(str(len(n)))