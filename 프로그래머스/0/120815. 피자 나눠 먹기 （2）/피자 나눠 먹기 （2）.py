def solution(n):
    for i in range(min(n, 6), n * 6 + 1, min(n, 6)) :
        if i % n == 0 and i % 6 == 0 :
            lcd = i
            break

    return lcd // 6