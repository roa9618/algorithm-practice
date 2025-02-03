import math

R = int(input())

if R > 0 and R <= 10000 :
    euclid = math.pi * (R ** 2)
    taxi = 2 * (R ** 2)

    print("%.6f" %euclid)
    print("%.6f" %taxi)