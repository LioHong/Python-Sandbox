def DiffEng2(values):
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
                return y - 1
            # Locates row of equal values

            elif seq[y][term] < 0:
                seq[y][term] = 0
            # Removes negative values
