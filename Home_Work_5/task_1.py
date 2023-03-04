def exponentiation(a, b):
    if b > 1:
        return exponentiation(a, b - 1) * a
    return a
print(exponentiation(2,3))

    

