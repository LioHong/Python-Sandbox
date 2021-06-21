def babbage():
    s = PolynGen()
    DiffEng3(s)

    return


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
            # Value of each x^n term
            values[x] += subtotal

    return values


def DiffEng3(values):
    i, j = 11, 12
    seq = [[0 for x in range(i)] for y in range(j)]
    seq[0] = [x for x in range(i)]  # Term numbers
    seq[1] = values  # Input values
    seq_zero = [0 for x in range(i)]  # For reference purposes

    for y in range(2, j):
        for term in range(i - 1):
            seq[y][term] = seq[y - 1][term + 1] - seq[y - 1][term]

            if seq[y] == seq_zero:
                for z in range(j):
                    print(seq[z])
                print("\n" + "The difference lies on row: ", end='')
                print(y - 1)
                return seq
            # Locates row of equal values

            elif seq[y][term] < 0:
                seq[y][term] = 0
            # Removes negative values


def PolynExtrap():
    babbage()
    seq
