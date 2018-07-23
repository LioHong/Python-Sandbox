'''
Name: multiple-arraylinks
I forgot how to write a docstring
Purpose: Work out how out to organise the code for dressup buttons.
Details: Garment button -(Unique mouseclick function)-> Handler symbol (-> Fitting frame)
The buttons, functions and handlers can each be put into their own array. The problem is putting the functions in.
There is also the need for placeholder outputs.
'''

def dsup():
    garmList = [2, 2, 2, 2, 2, 2]
    count = 0
    clickList = []
    for i in garmList:
        click = fooLister(i, count)
        count += 1
        print(count, click)
        clickList.append(click)
        print(clickList)

    print(clickList)

def fooLister(val1, val2):
    ans = val1 * val2**2
    return ans
