print('Hello World')

import numpy as np

myTuple = ('abc', np.arange(0, 3, 0.2), 2.5)

myTuple[0]
myTuple[1]
myTuple[2]


myList = ['abc', 'def', 'ghij']

myList.append('klm')

myList

myList2 = [1, 2, 3]
myList3 = [4, 5, 6]

myList2 + myList3


myArray2 = np.array(myList2)
myArray3 = np.array(myList3)

myArray2 + myArray3

myArray2.dot(myArray3) # = 1 * 4 + 2 * 5 + 3 * 6
