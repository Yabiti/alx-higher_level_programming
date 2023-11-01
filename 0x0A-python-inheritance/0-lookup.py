class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BianryTree(object):
    def __init__(self, root):
        self.root = node(root)
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "")
            traversal = self.preorder_print(self.left, traversal)
            traversal = self.preorder_print(self.right, traversal)
        return traversal


tree = BianryTree(1)
tree.root.left = node(2)
tree.root.right = node(3)

print(tree.print_tree("preoreder"))