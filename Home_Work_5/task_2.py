def summa(a,b):
    if b > 0:
        return summa(a,b - 1) + 1
    return a

print(summa(7,3))