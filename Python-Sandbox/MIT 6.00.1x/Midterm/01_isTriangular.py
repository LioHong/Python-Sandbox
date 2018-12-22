def is_triangular(k):
      """
      k, a positive integer
      returns True if k is triangular and False if not
      """
      '''
      Could be solved algebraically as well
      (n^2 + n)/2 = k
      But it will also require iteration. Maybe generate a few terms first
      and see if k lies in between them: 1, 10, 100, 1000, etc
      Then conduct bisection search until k equals one of the limits
      or k lies between two consecutive terms.
      '''
      count = 1
      copy = k
      if type(k) != int:
            print('Positive integers only!')


      elif k <= 0:
            print('Please input a positive integer!')

      else:
            while k > count:
                  k -= count
                  count += 1

            if k == count:
                  print(str(copy) + ' is a triangular number.')

            else:
                  print(str(copy) + ' is not triangular.')
