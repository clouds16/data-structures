

class Tester:
    def __init__(self, start= True, new = False):
        self.start = start
        self.new = new

    def getStart(self):
        return self.start

    def getNew(self):
        return self.new

def main():
    newTest = Tester()

    print(newTest.getStart())
    print(newTest.getNew())

if __name__ == '__main__':
    main()