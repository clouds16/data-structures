
def isMultiple(n, m):
    if n % m == 0 :
        return True
    else: 
        return False

def main():
    value  = isMultiple(int(input("Enter first value: ")), int(input("Enter second value: ")))
    if value :
        print("Is a multiple!")
    else:
        print("Is not a multiple!")

main()