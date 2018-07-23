"""
An old habit I forgot: annotating each file.
The goal was to make the computer guess the secret number of the user.
I had problems with shifting boundaries, so I kept thinking of ways
to tie it down. Eventually I realised that the next boundary was the
midpoint between the old ones and typed that in to reflect that.

I left the debug prints in.
Testing version control. Testing again
"""


def secretguess():
    maxi = 100
    lim1 = maxi
    lim2 = 0
    guess = int(abs(lim1 - lim2) / 2)
    mid = 0
    ans = ''

    print("Please think of a number between 0 and 100!")

    while ans != 'c':
        print("Is your secret number " + str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. " +
              "Enter 'l' to indicate the guess is too low. " +
              "Enter 'c' to indicate I guessed correctly. ")
        ans = input()

        if ans == 'l':
            lim2 = min(guess, lim1)
            mid = int((lim1 - lim2) / 2)
            guess = lim2 + mid
            print(lim1)
            print(lim2)

        if ans == 'h':
            lim1 = max(guess, lim2)
            mid = int((lim1 - lim2) / 2)
            guess = lim2 + mid
            print(lim1)
            print(lim2)

        # min() and max() prevent infinite loops

        if ans == 'h' and abs(lim1 - lim2) == 1:
            guess += 1

        if ans == 'quit':
            break

        if lim1 == lim2 or guess == lim1 or guess == lim2:
            # Flourish to prevent infinite loops
            ans = 'c'
            break

        elif ans != 'h' and ans != 'l' and ans != 'c':
            print("Sorry, I did not understand your input. Please type again.")

    if ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
