  
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

    def __repr__(self):
        return "data: {} , right child: {} , left child: {}".format(self.data, self.r_child , self.l_child)


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

def postOrder(root):
    if root != None:
        postOrder(root.r_child)
        postOrder(root.l_child)
        print(root)

def createBinaryTree(userList):

    r = Node(userList[0])
    userList = userList[1:]

    for i in range(len(userList)):
        binary_insert(r, Node(userList[i]))
    
    print("in order: ", )
    in_order_print(r)

    print("Pre order: ")
    pre_order_print(r)    

    print(r.__repr__)
    return r


def main():
    userList = [50, 30, 23, 11, 25, 35, 31, 42, 70, 80 , 73, 85]
    createBinaryTree(userList)
    

if __name__ == '__main__':
    main()


