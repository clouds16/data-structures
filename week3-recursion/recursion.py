def findMinAndMax(mylist): 
    
    def returnMax(mylist):
        if len(mylist) ==1:
            return mylist[0]
        else:
            return max(mylist[0], returnMax(mylist[1:]))

    def returnMin(mylist):
        if len(mylist) ==1:
            return mylist[0]
        else:
            return min(mylist[0], returnMin(mylist[1:]))
        
    return [returnMin(mylist), returnMax(mylist)]

def main():
    testList= [2,4,5,76,99,-3,5]
    print(findMinAndMax(testList))

main()

