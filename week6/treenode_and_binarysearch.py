

####################### Part 1 
#50, 30, 23, 11, 25, 35, 31, 42, 70, 80, 73, 85

        #               50
        #       30                70
        #    23        35       none    80
        # 11   25    31  42          73   85



class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None   
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False       

        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = TreeNode(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = TreeNode(data)
                return True




    def preorder(self):

        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):

        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
 
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = TreeNode(data)
            return True

    def preorder(self):
        if self.root is not None:
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            self.root.inorder()

    def postorder(self):
        if self.root is not None:
            self.root.postorder()

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(23)
    tree.insert(11)
    tree.insert(25)
    tree.insert(35)
    tree.insert(31)
    tree.insert(42)
    tree.insert(70)
    tree.insert(80)
    tree.insert(73)
    tree.insert(85)
    
    tree.inorder()
    print("in order:" )
    
    tree.preorder()
    print("pre order")
    
    tree.postorder()
    print("post order: ")