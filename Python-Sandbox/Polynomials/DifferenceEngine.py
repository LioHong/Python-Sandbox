def DiffEng(int):
    i, j = 11, 11
    seq = [[0 for x in range(i)] for y in range(j)]
    seq_zero = [0 for x in range(i)]
    # Initialises

    for y in range(j):
        seq[0][y] = y
    # Declares row of starting terms

    for val in range(j):
        seq[1][val] = val ** int
    # Declares row of exponented terms

    for x in range(2, i):
        for term in range(j - 1):
            seq[x][term] = seq[x - 1][term + 1] - seq[x - 1][term]

            if seq[x] == seq_zero:
                for z in range(i):
                    print(seq[z])
                print("\n" + "The difference lies on row: ", end='')
                return x - 1
            # Locates row of equal values

            elif seq[x][term] < 0:
                seq[x][term] = 0
            # Removes negative values
