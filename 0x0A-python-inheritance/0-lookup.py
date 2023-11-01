class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BianryTree(object):
    def __init__(self, root):
        self.root = node(root)