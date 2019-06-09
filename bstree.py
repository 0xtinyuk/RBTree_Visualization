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

    def pre_order_traversal(self, node):
        if node == None:
            return []

        result = [node.val]
        node.set_red_node()
        self.snapshot()
        node.set_black_node()
        result.extend(self.pre_order_traversal(node.left))
        result.extend(self.pre_order_traversal(node.right))
        return result

    def in_order_traversal(self, node):
        if node == None:
            return []

        result = self.in_order_traversal(node.left)
        node.set_red_node()
        self.snapshot()
        node.set_black_node()
        result.extend([node.val])
        result.extend(self.in_order_traversal(node.right))
        return result

    def post_order_traversal(self, node):
        if node == None:
            return []

        result = self.post_order_traversal(node.left)
        result.extend(self.post_order_traversal(node.right))
        node.set_red_node()
        self.snapshot()
        node.set_black_node()
        result.extend([node.val])
        return result
