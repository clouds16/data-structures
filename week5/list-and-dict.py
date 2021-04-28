#the difference between a list and a dict:
#lists are ordered , and are accessed by their position in the list, for example, a list will start with
# the 0th position and as it is filled, will append to the length of the list
# [2,3,4]

# a dictionary works as an unordered set, and data can be accessed by a key-value pair. 
# this key must be unique and can only appear once in the dictionary
# furthermore, dictionaries do not support sequence operations 

def createList():

    l = []

    while True:
        userInput = int(input("Enter a value to save to a list, -1 to break:  "))
        l.append(userInput)
        print(l)

        if userInput == -1 :
            break

    print("user generated list is now : ", l)
    
    while True:
        choice = int(input("Find a value based on its list position, enter -1 to exit : " ))
        print("the value at postion: " , choice , "is : ", l[choice])
        if choice ==-1 :
            break
        
    
def main():
    myDict = {
        "Name": "Hector",
        "Age" : 27,
        "Height": "5'10",
        "Car" : "Saturn",
        "Color": "Yellow",
        "Occupation" : "Engineer"
    }

    while True:
        print(myDict.keys())
        userIn = input("What parameter do you want to investigate?,q to exit ")
        
        if userIn == 'q':
            break
        print(myDict.get(userIn))


#createList()
main()