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
                print(userList)
            else : 
                c+=1
                print(userList)

    print("counter : " , c)  
    return userList

def insertSort(userList):
    n = len(userList)
    for i in range(n):
        value = userList[i]
        i = i-1
        while i>=0:
            if value < userList[i]:
                userList[i+1] = userList[i]
                userList[i] = value
                i = i-1
                print(userList)
            else:
                break
        
    return userList

def selectionSort(userList):
    n = len(userList)
    for i in range(0,n-1):
        smallest = i 
        
        for j in range(i+1, n):
            if userList[j] < userList[smallest]:
                smallest = j 
        if smallest != i:
            userList[i], userList[smallest] = userList[smallest], userList[i]
            print(userList)

    return userList

def main():
    l = [1,2,3,4,5,6,7,8,9,10]
    shuffle(l)
    # print("shuffled list is now: ", l)
    # print("bubble sorting: ", bubbleSort(l) )
    # print("reshuffling : ",shuffle(l))
    # print("insertion sort: ", insertSort(l) )
    print("reshuffling:", shuffle(l))
    print("selection sort: ", selectionSort(l))
    
    
    

main()