class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  

class Queue: 
      
    def __init__(self): 
        self.top = self.bottom = None
  
    def isEmpty(self): 
        return self.top == None

    def EnQueue(self, item): 
        newNode = Node(item) 
          
        if self.bottom == None: 
            self.top = self.bottom = newNode 
            return
        self.bottom.next = newNode 
        self.bottom = newNode 
 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        newNode = self.top 
        self.top = newNode.next
  
        if(self.top == None): 
            self.bottom = None
  

q = Queue() 
q.EnQueue(10) 
q.EnQueue(20) 
q.EnQueue(30) 
q.EnQueue(40) 
q.EnQueue(50)  
q.DeQueue()    
print("Queue top " + str(q.top.data)) 
print("Queue bottom " + str(q.bottom.data)) 
     