"""
Name: 07_closest_power
Author: Lio Hong
Date: 20180726
Goal:
      base: base of the exponential, integer > 1
      num: number you want to be closest to, integer > 0
      Find the integer exponent such that base**exponent is closest to num.
      Note that the base**exponent may be either greater or smaller than num.
      In case of a tie, return the smaller value.
      Returns the exponent.
Pseudocde:
      Check the difference between num and base**exp
      Select the minimum difference
Comments:
      Do I use list or dict in this case?
"""

def closest_power(base, num):
      if base <= 1 or num <= 0 or type(base) != int or type(num) != int:
            return 'Integers only! Base must be more than 1 and num more than 0!'
##      expo = [i for i in range(10)]
      #Don't really know how large power should be so I put 10.
      power = 16
      expo = [base**i for i in range(power)]
      diff = [0 for i in range(power)]
      print(expo)
      
      for i in range(power):
            diff[i] = abs(num - expo[i])
      print(diff)

      print(diff.index(min(diff)))

def randomeer():
      #Allows testing of closest_power()
      import random
      a = random.randint(1, 10)
      b = random.randint(100, 100000)
      print(str(a) + ', ' + str(b))
      closest_power(a,b)
