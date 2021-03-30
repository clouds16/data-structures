import time


class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.previous = None


class Deque:
    def __init__(self):
        self.start = None

    def isEmpty(self):
        return self.start == None

    def addFront(self, data):
        if self.start is None:
            newNode = Node(data)
            self.start = newNode
            print("node inserted")
            return
        newNode = Node(data)
        newNode.next = self.start
        self.start.previous = newNode
        self.start = newNode

    def addRear(self, data):
        if self.start is None:
            newNode = Node(data)
            self.start = newNode
            return
        n = self.start
        while n.next is not None:
            n = n.next
        newNode = Node(data)
        n.next = newNode
        newNode.previous = n

    def removeFront(self):
        if self.start is None:
            print("The list has no element to delete")
            return
        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start_prev = None

    def removeRear(self):
        if self.start is None:
            print("The list has no element to delete")
            return
        if self.start.next is None:
            self.start = None
            return
        n = self.start
        while n.next is not None:
            n = n.next
        n.previous.next = None

    def showList(self):
        if self.start is None:
            print("List has no element")
            return
        else:
            n = self.start
            while n is not None:
                print(n.item, " ")
                n = n.next


d = Deque()
d.addFront(6)
d.addFront(34)
d.addFront(2)
d.addRear(55)
d.addFront(-33)
d.addFront(6999)
d.removeRear()


d.showList()
d.removeFront()
time.sleep(2)
print("########################")
d.showList()
print(d.isEmpty())
