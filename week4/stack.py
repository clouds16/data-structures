class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self,data):
         
        if self.head == None:
            self.head= Node(data)
             
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
         
        if self.isempty():
            return None
             
        else:
     
            node_pop = self.head
            self.head = self.head.next
            node_pop.next = None
            return node_pop.data

    def peek(self):
         
        if self.isempty():
            return None
             
        else:
            return self.head.data
     
    # Prints out the stack     
    def display(self):
         
        all_nodes = self.head
        if self.isempty():
            print("Stack is Empty")
         
        else:
             
            while(all_nodes != None):
                 
                print(all_nodes.data,",",end = " ")
                all_nodes = all_nodes.next
            return



s = Stack()
s.push(10)
s.push(15)
s.push(3)
s.push("Stuff")
s.pop()
s.display()
