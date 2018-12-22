def charCounter(str):
    # Turns out this function is redundant when using a for
    # loop in the subsequent one
    # Anyway, the whole function already exists as str.count('substr')

    print('For inputted string: ' + str)
    char_count = 0
    for char in str:
        char_count += 1
    print("Char count is: ", end='')

    return char_count


def bobCounter(str):
    num_bob = 0
    n = 0

    for char in str:
        triplet = str[n:(n + 3)]
        if triplet == 'bob':
            num_bob += 1
        n += 1

    print('# of bob-s is ', end='')
    print(num_bob)
