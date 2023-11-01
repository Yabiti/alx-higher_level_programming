class node(object):
    def __int__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __inti__(self, root):
        self.root = node(root)

tree = BinaryTree(1)
tree.root.left = node(2)