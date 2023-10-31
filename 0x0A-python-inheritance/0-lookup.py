class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root= node(root)

tree = BinaryTree(1)
tree.root.left = node(2)
tree.root.left.left = node(3)
tree.root.left.right = node(4)
tree.root.right = node(5)
tree.root.right.left = node(6)
tree.root.right.right = node(7)