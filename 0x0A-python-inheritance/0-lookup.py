class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinatryTree(object):
    def __init__(self, root):
        self.root = node(root)