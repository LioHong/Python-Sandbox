"""
Name: 06_general_poly
Date: 20180725
Goal:
      L, a list of numbers (n0, n1, n2, ... nk)
      Returns a FUNCTION, which when applied to a value x,
      returns the value
      --> Known as 'Currying'
      (Define the other function inside, then return it.)
      n0 * x^k + n1 * x^(k-1) + ... nk * x^0
Pseudo-code:
      The function return makes things somewhat strange.
      Normally, I'd evaluate the list length and traverse it backwards.
      And increase the degree of x each time.

      But now there's something to be done with the coef beforehand.
Comments:
      Apparently return general_poly alone gives the object itself.
"""
      
L = [1, 2, 3, 4]
x = 10.5

def polyEval(x):
      def general_poly(L):
            deg = len(L)
            value = 0
            for coef in L:
                  value += coef * x**deg
                  deg -= 1
                  
            return value
      
      return general_poly(L)
