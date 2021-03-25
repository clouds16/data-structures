import time
import pandas as pd
import matplotlib.pyplot as plt

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def recur_fibo(n):

    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def testRecursive(n):
    print("Recursive Method")

    x= []
    t = []
    
    for i in range(n+1):
        start = time.time()
        recurr = recur_fibo(i)
        end = time.time()

        print("Fibonacci value: {0} fibb sum is {2} Time taken : {1}".format(i,end-start, recurr))
        x.append(i)
        t.append(end-start)

    return x, t


def testIterative(n):
    print("Iterative Method")
    x= []
    t = []
    
    for i in range(n+1):

        start = time.time()
        fib = f(i)
        end = time.time()

        print("Fibonacci value: {0}  fibb sum is {2} Time taken : {1}".format(i,end-start, fib))
        x.append(i)
        t.append(end-start)
        
    return x,t

def quickTest(n):
   start = time.time()
   rec  = recur_fibo(n)
   end = time.time()
   print(n , "time: ", end-start)

def main():

    usr = input("Quick test a value (q) or plot (p) multiple? ")

    if usr == 'p' or usr == 'P' :
        userIn = int(input("How many terms of the fibonacci sequence do you want to test:  "))
    
        x2, time2 = testIterative(userIn)
        x, timetaken= testRecursive(userIn)

        plt.plot(x, timetaken) 
        plt.plot(x2, time2)
        plt.xlabel("Term ")
        plt.ylabel("Time Taken To Perform Algorithm (seconds)")
        plt.title("Recursive (BLUE) vs Iterative (ORANGE) Time to Perform Algorithm ")
        plt.show()
    elif usr == 'q' or usr == 'P':
        quickTest(int(input("Test a Fibonnaci term:  ")))
    else: 
        print("Not one of program parameters")
main()


#