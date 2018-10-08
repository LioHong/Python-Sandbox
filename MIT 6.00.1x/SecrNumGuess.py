def secretguess():
    maxi = 100
    lim1 = maxi
    lim2 = 0
    guess = int(abs(lim1 - lim2) / 2)
    temp1, temp2 = 0, 0
    ans = ''
    print("Please think of a number between 0 and 100!")

    while ans != 'c':
        print("Is your secret number " + str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. " + \
              "Enter 'l' to indicate the guess is too low. " + \
              "Enter 'c' to indicate I guessed correctly. ")
        ans = input()

        if ans == 'h':
            guess = int(guess + abs(lim1 - guess) / 2)
            lim2 = min(lim1, guess)
            print(lim1)
            print(lim2)

        if ans == 'l':
            guess = int(guess - abs(guess - lim2) / 2)
            lim1 = max(lim2, guess)
            print(lim1)
            print(lim2)

        if ans == 'h' and abs(lim1 - lim2) == 1:
            guess += 1

        if ans == 'quit':
            break

        elif ans != 'h' and ans != 'l' and ans != 'c':
            print("Sorry, I did not understand your input. Please type again.")

    if ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
