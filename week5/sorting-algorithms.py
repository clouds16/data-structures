import random

def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]
    
    return a

def bubbleSort( userList ):
    n = len(userList)
    c = 0
    for i in range(0,n):
        for j in range(n - i - 1 ):
            if userList[j] > userList [j+1]:
                userList[j] , userList[j+1] = userList [j+1] , userList[j]
                c +=1

    

