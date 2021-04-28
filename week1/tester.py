import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    symb ="#"
  
    
    for i in range(0, n ):
        print(symb.rjust(n, " "))
        symb = symb +  "#"
    # Write your code here

if __name__ == '__main__':
    n = 6

    staircase(n)
