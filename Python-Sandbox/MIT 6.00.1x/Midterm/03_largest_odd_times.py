L = [3,9,5,3,5,3,9,5,9,13]

def largest_odd_times(L):
      """
      Date: 20180725
      Goal:
            Assumes L is a non-empty list of ints
            Returns the largest element of L that occurs an odd number 
            of times in L. If no such element exists, returns None
      
      """
      '''
      Today we learn that dictionary keys can also be int
      '''
      
      if type(L) != list:
            print('Lists only!')

      dict_L = {}
      
      for num in L:
           
            if num in dict_L:
                  dict_L[num] += 1

            else:
                  dict_L[num] = 1

      
      largest = max(dict_L)

      if dict_L[largest] %2 == 1:
            return largest
      
      else:
            return None
      
