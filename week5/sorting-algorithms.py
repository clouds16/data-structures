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
            else : 
                c+=1

    print("counter : " , c)  
    return userList

def insertSort(userList):
    n = len(userList)
    for i in range(n):
        key = userList[i]
        j = i-1
        while j >= 0 and key < userList[j] :
                userList[j + 1] = userList[j]
                print(userList)
                j -= 1
        userList[j + 1] = key
        
    return userList

def selectionSort(userList):
    n = len(userList)
    for i in range(n):
        for j in range(i+1, n):
            if userList[i] > userList[j]:
                userList[i], userList[j] = userList[j], userList[i]
                print(userList)

    return userList

def main():
    l = [1,2,3,4,5,6,7,8,9,10]
    shuffle(l)
    print("shuffled list is now: ", l)
    print("bubble sorting: ", bubbleSort(l) )
    print("reshuffling : ",shuffle(l))
    print("insertion sort: ", insertSort(l) )
    print("reshuffling:", shuffle(l))
    print("selection sort: ", selectionSort(l))
    
    
    

main()
