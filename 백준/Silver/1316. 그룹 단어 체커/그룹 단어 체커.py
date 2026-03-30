import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n) :
    dup = []
    word = list(sys.stdin.readline().rstrip())
    is_group = True

    for i in range(len(word)) :
        if word[i] not in dup :
            dup.append(word[i])
        else :
            if word[i - 1] != word[i] :
                is_group = False
                break
        
    if is_group :
        count += 1

sys.stdout.write(str(count))