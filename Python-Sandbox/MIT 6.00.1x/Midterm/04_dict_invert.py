d1 = {1:10, 2:20, 3:30}
##returns {10: [1], 20: [2], 30: [3]}
d2 = {1:10, 2:20, 3:30, 4:30}
##returns {10: [1], 20: [2], 30: [3, 4]}
d3 = {4:True, 2:True, 0:True}
##returns {True: [0, 2, 4]}

def dict_invert(d):
      """
      Date: 20180725
      Goal:
            d: dict
            Returns an inverted dictionary according to the instructions above.
      Comments:
            In the end, try-except was the only way to handle the KeyError.
            I just forced the error to appear by typing the value-less keyInv.
      """
      dInv = {}

      if type(d) != dict:
            print('Dictionaries only! NEXT!')

      
      else:
            for key in d:
                  keyInv = d[key]
                  try:
                        type(dInv[keyInv])
                        
                  except KeyError:
                        dInv[keyInv] = [key]
                        
                  else:
                        dInv[keyInv].append(key)
                  
            return dInv


##            if type(dInv[keyInv]) != list:
##                  dInv[keyInv] = [key]
##
##            else:
##                  dInv[keyInv].append(key)

