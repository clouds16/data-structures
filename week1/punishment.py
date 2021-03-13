
def punishment( repetition):
    punishment_line = "I will never spam my friends again!"
    
    while repetition > 0 :
        print(punishment_line)
        repetition -= 1
        

def main():
    punishment(int(input("How many times will the line be repeated: ")))

main()