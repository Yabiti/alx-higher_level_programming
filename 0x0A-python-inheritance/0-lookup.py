class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinatryTree(object):
    def __init__(self, root):
        self.root = node(root)

tree = BinatryTree(1)
tree.root.left = node(2)
tree.root.left.right = node(3)
tree.root.left.left = node(4)
tree.root