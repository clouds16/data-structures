
def isMultiple(n, m):
    #will check if there are any remainders, if there are no remainders , values are multiples
    if n % m == 0 :
        return True
    #values are not multiples, returns a false
    else: 
        return False

def main():
    #will prompt the user for a multiples, multiples should be an integer 
    multiples  = isMultiple(int(input("Enter first multiples: ")), int(input("Enter second multiples: ")))
    #if multiples is true, print to prompt that the program found multiples
    if multiples :
        print("Is a multiple!")
    #print that no multiples were found 
    else:
        print("Is not a multiple!")

main()