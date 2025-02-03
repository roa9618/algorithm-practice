def hansu_check(N) :
    N = str(N)
    num = []
    total = []

    for i in N :
        num.append(int(i))

    for i in range(len(num) - 1) :
        total.append(num[i + 1] - num[i])

    if len(num) == (total.count(sum(total) / len(total)) + 1) :
        return 1
    else :
        return 0

N = int(input())

count = 99

if N > 0 and N < 100 :
    count = N
elif N > 99 and N < 1001 :
    for i in range(100, N + 1) :
        if hansu_check(i) == 1 :
            count += 1
        else :
            continue

print(count)