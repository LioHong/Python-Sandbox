'''
Possible config option for slime spawning in biomes
'''

COLOURS_FILE = "minecraft_colours.txt"

def loadColours():
      '''
      The text file contains colour names, colour decimal IDs and colour
      abbreviations I set myself.
      So the user can choose to use either the full names or their abrv.
      '''
      inFile = open(COLOURS_FILE, 'r')
      line = inFile.readline()
      colourList = line.split()
      colourName = colourList[:16]
      colourAbrv = colourList[-16:-1]
      colourMix = []

      #Previous attempts at combining list entries to be human-readable
      #colourMix = [colourName[i] + colourAbrv[i] for i in range(colourName)]
      #["{}{:02}".format(colourName_, colourAbrv_) for colourName_, colourAbrv_ \
      # in zip(colourName, colourAbrv)]
      
      for i in zip(colourName,colourAbrv):
            temp = i[0].capitalize() + ' ' + i[1]
            colourMix.append(temp)
      print(colourMix)
            
      return colourName, colourAbrv, colourMix
      #Returned as a tuple of three lists

def occur():
      '''
      In the actual config file it won't be so interactive.
      However the input should still work the same way, and processing it
      will have to happen as the game boots up.

      The code here is very long. Might have to split into sub-functions.
      But it works.
      So much time was spent on foolproofing the user input.
      So many for loops btw, with the same condition even. Might be able to
      combine them later on.
      '''
      baseSpawn = 1
      coloursNum = 16
      colours = loadColours()
      perc = 0
      subT = 0
      subTot = []
      
      biomeBoost = input('Select the biome for spawn boosting: ')
      print('-'*10)
      print('Which colours of slime do you want to boost, and by how much?')
      print('Type in the colour as well as the number in the same line.')
      print('A raw number indicates how many times spawning will be boosted.')
      print('A percentage(%) will directly alter the chance of spawning.')
      print('Possible format: COL ##, COL ##%')

      dash = '-' * 10
      print(dash)
      print('You may type in the name or abbreviation as below:')
      for i in colours[2]:
            print(i)
      print(dash)
      
      boostStr = input('Your answer: ')
      boostList = boostStr.split(',')
      boostedList = [i.split() for i in boostList]

      #Processes data into computer-readable form
      for i in boostedList:
            if len(i[0]) == 2:
                  temp = i[0].upper()
                  temp2 = colours[1].index(temp)
                  i[0] = colours[0][temp2]

            #Trash condition to place this above error statement
            elif len(i[0]) > 2:
                  i[0] = i[0].lower()

            elif i[0] not in colours[0] or i[0] not in colours[1]:
                  print("That colour can't be found! Please try again.")
                  break

      #Changes spawn rates based on inputted values
      cNumDefault = coloursNum - len(boostedList)
      for i in boostedList:
            if i[1][-1] == '%':
                  i[1] = float(i[1][:-1])/100
                  perc += i[1]

            else:
                  i[1] = float(i[1])
                  subT += i[1]
                  subTot.append(i[1])
                  #This list allows for float multipliers to be inputted

      subT += baseSpawn * cNumDefault
      basePerc = round((baseSpawn/subT * (1 - perc)),3)
      
      for i in boostedList:
            if i[1] in subTot:
                  i[1] = i[1]/subT * (1 - perc)
                  i[1] = round(i[1],3)

      #A dictionary makes calling the values more elegant            
      colDict = {}
      for i in boostedList:
            colDict[i[0]] = i[1]
      print(dash)
      for colr in colours[0]:
            if colr in colDict.keys():
                  print('{:<10s}{:>1s}'.format(colr.upper(),': '), end='')
                  temp = round(colDict[colr]*100,3)
                  print('{:>6s}'.format(str(temp) + '%'))          
            else:
                  print('{:<10s}{:>1s}'.format(colr.capitalize(),': '), end='')
                  temp = round(basePerc*100,3)
                  print('{:>6s}'.format(str(temp) + '%'))                      
