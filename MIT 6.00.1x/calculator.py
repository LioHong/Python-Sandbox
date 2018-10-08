def mul(multiplier, multicand):
    pdt = 0
    for a in range(multicand):
        pdt += multiplier
    return pdt


# Only works with int because of range()

def div(dividend, divisor):
    quotient = 0
    remainder = dividend
    for b in range(1000):
        if remainder >= divisor:
            remainder -= divisor
            quotient += 1
    return quotient, remainder


# This function returns a remainder, not a decimal/fraction

def pwr(base, exponent):
    power = base
    for c in range(exponent - 1):
        power = mul(base, power)
    return power


# Gets laggy

def pwr2(base, exponent):
    power = base
    for d in range(exponent - 1):
        power *= base
    return power


# Less laggy when using '*' but still slower than pow()

def sqr(base):
    square = mul(base, base)
    return square


# Same responsiveness as pow(base,2)

def sqrt(num):
    guess = 1
    for i in range(1000):
        if pwr2(i, 2) <= num:
            guess = i
            holder = i

        elif round(guess ** 2) != num:
            holder2 = (guess + num / guess)
            guess = holder2 / 2

    return round(guess, 3)


# Sadly this was unable to work with my div() because of TypeError
# Still doesn't work with smaller numbers (<1, near 1)

'''
Might add trig functions, pi and e in the future.
'''
