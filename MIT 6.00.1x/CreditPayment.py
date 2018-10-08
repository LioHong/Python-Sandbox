def CredPay(initBal, annIntRate, mthPay):
    while countMth < 12:
        mthPay = mthPayRate * bal
        mthUnpBal = bal - mthPay
        bal = mthUnpBal * (1 + mthIntRate)
        countMth += 1

    return bal, m


def CredPayMin(initBal, annIntRate, mthPayRate):
    '''
    One of the assignments from edX. They went through the equations in detail
    and provided test cases so it was pretty straightforward.
    '''

    mthIntRate = annIntRate / 12.0
    bal = initBal
    countMth = 0
    finBal = bal

    while countMth < 12:
        mthPay = mthPayRate * bal
        mthUnpBal = bal - mthPay
        bal = mthUnpBal * (1 + mthIntRate)
        countMth += 1

    print("Remaining balance: " + str(round(bal, 2)))


def CredPayOff(initBal, annIntRate):
    '''
    Calculates the minimum fixed monthly payment needed in order pay off a
    credit card balance within 12 months. By a fixed monthly payment, we
    mean a single number which does not change each month, but instead is a
    constant amount that will be paid each month.

    Assume that the interest is compounded monthly according to the balance
    at the end of the month (after the payment for that month is made). The
    monthly payment must be a multiple of $10 and is the same for all months.
    Notice that it is possible for the balance to become negative using this
    payment scheme, which is okay.

    At first I considered bisection search, but it seems that incrementing
    the payment is expected for this. Very well, bisection search hasn't been
    good to me anyway.

    Final check is when the final balance becomes negative. So ascending
    should be fine. To narrow the search range, I can take initBal/12 since
    the monthly payment will surely be higher than that.

    OK that was simple enough. Simple iteration exercise.
    Now solving it recursively, that's interesting.
    '''

    mthIntRate = annIntRate / 12.0
    bal = initBal
    mthPay = (initBal / 12) // 10 * 10
    countGuess = 0

    while bal >= 0:
        bal = initBal
        countMth = 0

        CredPay(initBal, annIntRate, mthPay)

        countGuess += 1
        mthPay += 10

    mthPay = round(mthPay) - 10
    print("Lowest Payment: " + str(mthPay))
    print("Found in " + str(countGuess) + " guesses")


def CredPORec(initBal, annIntRate, mthPay=0):
    '''
    Recursive version of above
    I couldn't think of how to break down this problem into smaller pieces
    so I looked at some shared code. And they simply incremented the payment!
    Of course, it's so simple now that I know it.

    I set mthPay at the default value of 0 to avoid having the user input it.
    I tried to declare it in terms of initBal but that went badly. I kept
    getting NameError.

    Seems like I'm running into trouble intialising variables. If I run the
    declaration in #, I get an infinite loop because mthPay remains constant.
    Same happens with countGuess, so I can't even see how many iterations
    occured. Well I can infer it from the final payment value given, actually.

    Hmmm, what can I take away from this? What can I say?
    How recursion automatically involves a change to the variable in some
    regular manner. Kind of like what I've been seeing past students do with
    list comprehension to massively compact their code.
    Incidentally the functionality of recursive functions overlaps with
    while loops. So it might be fruitful to consider how I could rewrite
    while loops as recursion.

    Both examples didn't use default values for mthPay, but they did include
    it. I took inspiration from the student's pseudocode, while the TA's
    seems to reference their past function to calculate the balance, and then
    recurve that also before recursing the mthPay calculation.
    So I guess that proves that the first part CAN be recursed after all.
    '''

    mthIntRate = annIntRate / 12.0
    bal = initBal
    # mthPay = (initBal / 12) // 10 * 10
    countGuess = 0
    month = 0

    while month < 12:
        mthUnpBal = bal - mthPay
        bal = mthUnpBal * (1 + mthIntRate)
        month += 1

    if bal > 0:
        CredPORec(initBal, annIntRate, mthPay + 10)
        countGuess += 1

    else:
        print("Lowest Payment: " + str(mthPay))


def CredPOBi(initBal, annIntRate):
    '''
    Well.
    Now I know why the first part was so easy.
    It's OK actually because they went through the maths to find an upper
    bound. Kind of. It was non-trivial, but I still have to do the search.
    '''

    mthIntRate = annIntRate / 12.0
    bal = initBal
    mthPayLow = initBal / 12.0
    mthPayHi = initBal * (1 + mthIntRate ** 12) / 12.0
    mthPayMid = mthPayLow + (mthPayHi - mthPayLow) / 2.0
    countGuess = 0
