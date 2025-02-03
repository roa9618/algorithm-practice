sen = str(input().upper())

word = []
count = []
max = 0
check = 0

if len(sen) <= 1000000 :
    for i in sen :
        word.append(i)

    word = list(set(word))
    word.sort()

    for i in word :
        count.append(sen.count(i))

    for i in count :
        if i > max :
            max = i
            check = 0
        elif i < max :
            continue
        elif i == max :
            check += 1
    
    if check > 0 :
        print("?")
    else :
        print(word[count.index(max)])