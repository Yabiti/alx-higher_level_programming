class node(object):
    def __inti__(self, value):
        self.value = value
        self,left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = node(root)