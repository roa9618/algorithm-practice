x, y, w, h = map(int, input().split())

num = [x, y]
num.append(w - x)
num.append(h - y)

print(min(num))