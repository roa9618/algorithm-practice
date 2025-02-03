n = int(input())
cycle = 1
ten = n // 10
one = n % 10
new = 0

if n != 0 :
    while True :
        if n == new :
            break
        else :
            new = ((ten + one) % 10) + (one * 10)
            one = new % 10
            ten = new // 10
            cycle = cycle + 1
else :
    cycle = 2
print(cycle-1)