def VowelCounter(str):
    numVowels = 0
    for char in str:
        if char == 'a' or char == 'e' or char == 'i' \
                or char == 'o' or char == 'u':
            numVowels += 1
    print('# of Vowels: ', end='')
    print(numVowels)
