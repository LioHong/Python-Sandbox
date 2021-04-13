# -*- coding: utf-8 -*-
"""
Filename: roman_numeric_converter_twoway.py
Date created: Tue Apr 13 21:17:41 2021
@author: Julio Hong
Purpose: Converts from Hindu-Arabic numerals to Roman numerals and vice-versa.
(Note: Apparently Roman numerals didn't necessarily adhere to subtractive notation but I'll assume as such.)
Notice how the functions build on each other.
Imagine what other number systems this concept could be applied. Number systems both archaic and alien.
Maybe even non-decimal number systems. Could take inspiration for converts for binary (2), octal (8), hexademical (16) and duodecimal (12).

Inspired by https://www.reddit.com/r/learnpython/comments/mmuwk4/6_months_in_and_my_1st_python_app_is_up_and/
Babylonian: https://www.dcode.fr/babylonian-numbers
Cistercian (EU monks): https://www.dcode.fr/cistercian-numbers

Steps: 
	Thousands	Hundreds	Tens	Units
1	M	C	X	I
2	MM	CC	XX	II
3	MMM	CCC	XXX	III
4		CD	XL	IV
5		D	L	V
6		DC	LX	VI
7		DCC	LXX	VII
8		DCCC	LXXX	VIII
9		CM	XC	IX

Max value possible with this system is 3999 or MMMCMXCIX, because no value for 4000 exists.

"""

# Break down Hindu-Arabic numerals into powers of ten.
# Ones: I, Tens: X, Hundreds: C, Thousands: M
# Five: V, Fifty: L, Five hundred: D
# Is there a consistent way to run subtractive notation, and also account for the fives?
# If 5 is present, then add on the basic unit notation to its right.

def decompose_num(num):
    # Make sure the number isn't too large to convert
    # if num >= 4000:
    if num >= 8999999:
        return 'Number too large to convert into Roman numerals. Max value is 3999.'

    # Breaks up a given number into its component numbers based on the digits place.

    power_of_ten = 1
    component_nums = []

    while num != 0:
        # Run a division and modulo.
        remainder = num % 10
        # Restore the order of magnitude.
        component_nums.append(remainder * power_of_ten)

        # Then divide the quotient by ten and repeat.
        quotient = num // 10
        num = quotient
        power_of_ten *= 10

    return component_nums

# rom_dict = {'ones': {1:'I', 5:'V'},
#             'tens': {10:'X', 50:'L'},
#             'hundreds': {100:'C', 500:'D'},
#             'thousands': {1000:'M'}}
# rom_dict = {1:'I', 5:'V',
#             10:'X', 50:'L',
#             100:'C', 500:'D',
#             1000:'M'}
rom_dict = {1:'I', 5:'V',
            10:'X', 50:'L',
            100:'C', 500:'D',
            1000:'M', 5000:'N',
            10000:'W', 50000:'Y',
            100000:'A', 500000:'H',
            1000000:'E', 5000000:'G'}
# Imaginary Roman symbols.
# Wan for 10,000, lakh for 100,000, mega for 1,000,000

# Start with the basic additive notation.
def roman_convert_simple(num):
    roman_num_simple = ''
    # Break up the number input.
    component_nums = decompose_num(num)
    for val in component_nums:
        # Note that the order of magnitude of each element corresponds to its index.
        order_of_magnitude = component_nums.index(val)
        power_of_ten = 10 ** order_of_magnitude
        place = ''
        # digit determines number of times to repeat the Roman numeral.
        digit = val // power_of_ten
        for i in range(digit):
            place += rom_dict[power_of_ten]

        # If I simply concatenate the chars, the outputted Roman numeral will be reversed.
        roman_num_simple = place + roman_num_simple


    return roman_num_simple

# Now include the special notation for 5.
def roman_convert_with_fives(num):
    roman_num_fives = ''
    # Break up the number input.
    component_nums = decompose_num(num)
    for val in component_nums:
        # Note that the order of magnitude of each element corresponds to its index.
        order_of_magnitude = component_nums.index(val)
        power_of_ten = 10 ** order_of_magnitude
        place = ''
        # digit determines number of times to repeat the Roman numeral.
        digit = val // power_of_ten
        if digit > 4:
            place = rom_dict[power_of_ten * 5]
            digit -= 5

        for i in range(digit):
            place += rom_dict[power_of_ten]

        # If I simply concatenate the chars, the outputted Roman numeral will be reversed.
        roman_num_fives = place + roman_num_fives

    return roman_num_fives

# Include the subtractive notation for powers of ten, and fives.
def roman_convert_subtract(num):
    # I could hardcode for 4, 9, 40...
    # But a rule would be more flexible especially if I add more symbols for higher powers of ten.
    roman_num_sub = ''
    # Break up the number input.
    component_nums = decompose_num(num)
    for val in component_nums:
        # Note that the order of magnitude of each element corresponds to its index.
        order_of_magnitude = component_nums.index(val)
        power_of_ten = 10 ** order_of_magnitude
        place = ''
        # digit determines number of times to repeat the Roman numeral.
        digit = val // power_of_ten

        if (digit % 10) == 4:
            place = rom_dict[power_of_ten] + rom_dict[power_of_ten * 5]

        elif (digit % 10) == 9:
            place = rom_dict[power_of_ten] + rom_dict[power_of_ten * 10]

        else:
            if digit > 4:
                place = rom_dict[power_of_ten * 5]
                digit -= 5

            for i in range(digit):
                place += rom_dict[power_of_ten]

        # If I simply concatenate the chars, the outputted Roman numeral will be reversed.
        roman_num_sub = place + roman_num_sub

    return roman_num_sub

# Now to convert from Roman numerals to Hindu-Arabic.
# Fives will definitely remain within the same order of magnitude.
# Ones also behave the same, but the subtractive notation makes this tricky. Might want to build up from simple first.

# I want to avoid hardcoding as much as possible. So no searching for symbols based on rom_dict.
# Especially concerning fours and nines, due to subtractive notation.
# Instead, maybe traverse the string for each order of magnitude.
# Stop when the length of the substrings equals the total length of the original string.
def hindarab_convert_simple(rom_num_simple):
    power_of_ten = 1
    cumul_length = 0
    hindarab_num_simple = 0

    while cumul_length != len(rom_num_simple):
        # Count the number of ones.
        count_ones = rom_num_simple.count(rom_dict[power_of_ten])
        # Record the number of evaluated symbols.
        cumul_length += count_ones
        # Add to converted total.
        hindarab_num_simple += count_ones * power_of_ten
        # Increase order of magnitude.
        power_of_ten *= 10

    return hindarab_num_simple

# Include fives.
def hindarab_convert_fives(rom_num_fives):
    power_of_ten = 1
    cumul_length = 0
    hindarab_num_fives = 0

    while cumul_length != len(rom_num_fives):
        # Count the number of ones.
        count_ones = rom_num_fives.count(rom_dict[power_of_ten])
        # Record the number of evaluated symbols.
        cumul_length += count_ones

        # Count the number of fives.
        count_fives = rom_num_fives.count(rom_dict[power_of_ten * 5])
        cumul_length += count_fives

        # Add to converted total.
        hindarab_num_fives += (count_ones + count_fives * 5) * power_of_ten
        # Increase order of magnitude.
        power_of_ten *= 10

    return hindarab_num_fives

# Include subtractive notation. This did not work because of list-indexing errors.
def hindarab_convert_sub(rom_num_fives):
    power_of_ten = 1
    cumul_length = 0
    hindarab_num_sub = 0

    while cumul_length != len(rom_num_fives):
        # The first occurrence of the ones symbol may be followed by another ones symbol.
        # Or a five symbol or tens symbol.
        # Split at first occurrence.
        sub_nota_checklist = rom_num_fives.split(rom_dict[power_of_ten])
        print(sub_nota_checklist)
        print(sub_nota_checklist[1][0])
        try:
            # Check first char of second substring. Most likely to be blank.
            # Then proceed as before
            if sub_nota_checklist[1] == '':
                # Count the number of ones.
                count_ones = rom_num_fives.count(rom_dict[power_of_ten])
                # Record the number of evaluated symbols.
                cumul_length += count_ones

                # Count the number of fives.
                count_fives = rom_num_fives.count(rom_dict[power_of_ten * 5])
                cumul_length += count_fives

                # Add to converted total.
                hindarab_num_sub += (count_ones + count_fives * 5) * power_of_ten

            # Elif: Is it 5?
            elif sub_nota_checklist[1][0] == rom_dict[power_of_ten * 5]:
                cumul_length += 2
                hindarab_num_sub += 4

            # Elif: Is it 10?
            elif sub_nota_checklist[1][0] == rom_dict[power_of_ten * 10]:
                cumul_length += 2
                hindarab_num_sub += 9

            # Increase order of magnitude.
            power_of_ten *= 10

        except IndexError:
            # Increase order of magnitude.
            power_of_ten *= 10


    return hindarab_num_sub

# Second attempt by removing nines.
# Note: Due to referencing a higher power of 10, this Hindu-Arabic converter can only convert for values up to 999,999.
# Vs. up to 9,999,999 for the Roman converter.
def hindarab_convert_sub2(rom_num_fives):
    power_of_ten = 1
    cumul_length = 0
    hindarab_num_sub = 0
    temp_rom = rom_num_fives

    while cumul_length != len(rom_num_fives):
        # The first occurrence of the ones symbol may be followed by another ones symbol.
        # Or a five symbol or tens symbol.
        fours_check = rom_dict[power_of_ten] + rom_dict[power_of_ten * 5]
        nines_check = rom_dict[power_of_ten] + rom_dict[power_of_ten * 10]

        if temp_rom.count(fours_check) == 1:
            cumul_length += 2
            hindarab_num_sub += 4 * power_of_ten

        elif temp_rom.count(nines_check) == 1:
            cumul_length += 2
            hindarab_num_sub += 9 * power_of_ten
            # Remove extra tens symbol.
            temp_rom = temp_rom.replace(nines_check, '')

        # Then proceed as before
        else:
            # Count the number of ones.
            count_ones = temp_rom.count(rom_dict[power_of_ten])
            # Record the number of evaluated symbols.
            cumul_length += count_ones

            # Count the number of fives.
            count_fives = temp_rom.count(rom_dict[power_of_ten * 5])
            cumul_length += count_fives

            # Add to converted total.
            hindarab_num_sub += (count_ones + count_fives * 5) * power_of_ten

        # Increase order of magnitude.
        power_of_ten *= 10


    return hindarab_num_sub
