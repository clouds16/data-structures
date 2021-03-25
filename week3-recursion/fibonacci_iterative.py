import time 


def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def main():
    print("Iterative Version")
    start = time.time()
    print(40)
    end = time.time()
    print(end- start)

main()