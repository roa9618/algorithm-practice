array = map(int, input().split())

sum = 0

for i in array :
    sum += i ** 2

print(sum % 10)