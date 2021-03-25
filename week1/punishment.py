
def punishment( repetition):
    punishment_line = "I will never spam my friends again!"
    
    #while loop will run until t he repetition value is 0 
    while repetition > 0 :
        print(punishment_line)
        #iterator that will update the repetition value
        repetition -= 1
        
#main loop to separate the concerns - will execute program
def main():
    #punishment(int(input("How many times will the line be repeated: ")))
    
    punishment(100)

main()