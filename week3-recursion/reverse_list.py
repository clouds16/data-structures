def reverseList(mylist):
    if len(mylist) ==1:
        return [mylist[0]]
    else:
        return [mylist[-1]] + reverseList(mylist[:-1])

def main():
    l = [1,2,3,4,5,6,7,8,9,10,11]
    print(reverseList(l))
    #print(reverseAList(l))
 

main()

