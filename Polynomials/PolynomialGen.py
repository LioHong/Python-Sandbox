def PolynGen():
    import random

    num = 11
    powerList = [random.randint(0, 9) for x in range(num)]
    coefList = [random.randint(0, 9) for x in range(num)]
    seq = [x for x in range(num)]
    values = [0 for x in range(num)]

    for x in range(num):
        for y in range(num):
            subtotal = coefList[y] * seq[x] ** powerList[y]
            values[x] += subtotal

    return values
