class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self, root):
        self.root = node(root)
    
    def preorder_print(self, start, )

tree = BinaryTree(1)
tree.root.left = node(2)
tree.root.right = node(3)
tree.root.left.left = node(4)