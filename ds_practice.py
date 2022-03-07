from argparse import _MutuallyExclusiveGroup
from datetime import MAXYEAR
import re


myString = list(input()) 

while True : 
    if myString[0] == '=' : 
        myString.pop(0)
    else : 
        break

myStack = []

for i in range(len(myString)) : 
        if myString[i] != "=" : 
            myStack.append(myString[i])
        else :
            myStack.pop() 
        
            


print(''.join(myStack))














