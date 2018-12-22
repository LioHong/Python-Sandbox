test = 'Felt like participating in the #artistvsartmeme'

def print_without_vowels(s):
      '''
      s: the string to convert
      Finds a version of s without vowels and whose characters appear in the 
      same order they appear in s. Prints this version of s.
      Does not return anything
      '''
      if type(s) != str:
            print('Strings only!')

      vowels = ['a', 'e', 'i', 'o', 'u']
      deVoweled = []
      
      for char in s:
            if char not in vowels:
                  deVoweled.append(char)

      return ''.join(deVoweled)
