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

M = int(input())
N = int(input())

num_list = []

if M <= 10000 and N <= 10000 :
    for i in range(M, N + 1) :
        val = check(i)
        if val == 1 :
            num_list.append(i)
        else :
            continue
    if len(num_list) > 0 :
        print(sum(num_list))
        print(min(num_list))
    else :
        print(-1)