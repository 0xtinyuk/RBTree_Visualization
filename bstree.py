from tree_plt import save_rb_tree
from rbtree import RBTree, RBTreeNode


class BSTreeNode(RBTreeNode):
    def __init__(self, val, color="B"):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class BSTree(RBTree):

    def left_rotate(self, node):
        pass

    def right_rotate(self, node):
        pass

    def check_node(self, node):
        pass

    def check_delete_node(self, node):
        pass
