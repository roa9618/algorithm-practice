def check(number) :
    if number < 2 :
        return 0
    elif number == 2 :
        return 1
    else :
        for i in range(2, number) :
            if number % i == 0 :
                return 0
                break
            else :
                continue
        return 1

N = int(input())

count = 0

if N <= 100 :
    num = list(map(int, input().split()))
    if N == len(num) :
        for i in num :
            val = check(i)
            if val == 1 :
                count += 1
            else :
                continue
    print(count)