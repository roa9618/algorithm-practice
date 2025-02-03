a, b, c = map(int, input().split(" "))

num = [a, b, c]

if a == b :
  if b == c :
    print(10000 + (a * 1000))
  elif b != c :
    print(1000 + (a * 100))
elif a != b :
  if b == c :
    print(1000 + (b * 100))
  elif b != c and a != c :
    print(max(num) * 100)
  elif b != c and a == c :
    print(1000 + (a * 100))