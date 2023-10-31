class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinatryTree(object):
    def __init__(self, root):
        self.root = node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        else:
            print("traversal_type" + str(traversal_type) + "is not supported")
            return False


    def preorder(self, start, traversal):
        if start:
            traversal += (str(start.value, + "-"))
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
tree = BinatryTree(1)
tree.root.left = node(2)
tree.root.left.right = node(3)
tree.root.left.left = node(4)
tree.root.right = node(5)
tree.root.right.left = node(6)
tree.root.right.right.right = node(7)
tree.root.right.right.left = node(8)

print(tree.print_tree("preorder"))




