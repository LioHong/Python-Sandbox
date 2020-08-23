# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:14:06 2020

@author: Julio Hong
"""
# Exploring hyperoperations
# The methods below have the same format, but I can't quite recurse them.
# hyperop Library: https://github.com/thoppe/python-hyperoperators
import decimal
from hyperop import hyperop
# Use as H# = hyperop(#), where H1 is addition.
# Works via recursion

# a + b
def add_nums(num1, num2):
    return num1 + num2

# a * b
def multiply_nums(num1, num2):
    ans = num1
    for i in range(num2-1):
        ans = add_nums(ans, num1)
    return ans

# a^b or a↑b (Alt+24)
def power_nums(num1, num2):
    ans = num1
    for i in range(num2-1):
        ans = multiply_nums(ans, num1)
    return ans

# a^a^...^a for b times or a↑↑b
def tetrate_nums(num1, num2):
    ans = num1
    for i in range(num2-1):
        ans = power_nums(ans, num1)
    return ans

# tetrate_nums(2,7) fails because I guess it's just too many operations
# If I simplify to power:
# fourate_nums(2,16) fills the entire console screen at default zoom + max size: '1.415461e+9864'
# fourate_nums(2,22) = '4.544297e+631305', which makes even the scinote code stumble.
# Can understand this as the square of the previous term.
def fourate_nums(num1, num2):
    ans = num1
    for i in range(num2-1):
        ans = ans**num1
    return ans

# Greek again lol, just call it fivate why don't you
# a tetrated by a for b times or a↑↑↑b or a[5]b
# I cannot even comprehend it. I need to before I sleep.
# This might be wrong.
def pentate_nums(num1, num2):
    ans = num1
    for i in range(num2-1):
        ans = tetrate_nums(ans, num1)
    return ans

# Doesn't actually work but it keeps this code safe
# Shows to 2 dp
def large_num_scinote(large_long):
    d = decimal.Decimal(large_long)
    format(d, '.2e')



# Maybe there's a way to recurse these operations
#def recurve_op(num1, num2, operation):
#    ans = num1
#    for i in range(num2-1):
#        ans = operation(ans, num1)
#    return ans
#
#def multiply_nums(num1, num2):
#    recurve_op(num1, num2)
#    
#def power_nums(num1, num2):
#    ans = num1
#    for i in range(num2-1):
#        ans = multiply_nums(ans, num1)
#    return ans
