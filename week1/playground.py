import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    sumArr = []
    # Write your code here
    for i in range(len(arr)):
        total = sum(arr) - arr[i]
        sumArr.append(total)
    
    for i in range(len(sumArr)):
        
        minimum = maximum = sumArr[0]
        
        if sumArr[i] < minimum :
            minimum = sumArr[i]
        if sumArr[i] > maximum :
            maximum = sumArr[i]
    
    print(minimum)
    print(maximum)
    
    return min, max

if __name__ == '__main__':

    arr = [1,2,3,4,5,6,7]

    miniMaxSum(arr)