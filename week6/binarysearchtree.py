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


r = Node(5)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(4))

in_order_print(r)
print("#######")
pre_order_print(r)


print(r.__repr__)