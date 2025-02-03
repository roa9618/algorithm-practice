n = int(input())
score = list(map(float, input().split(" ")))
max_score = 0
sum = 0

max_score = max(score)
    
for j in range(n) :
    sum = sum + ((score[j] / max_score)*100)

total = sum / n

print(total)