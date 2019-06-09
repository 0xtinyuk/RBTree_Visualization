from tree_plt import save_tree


class RBTreeNode:
    def __init__(self, val, color="R"):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def is_black_node(self):
        return self.color == "B"

    def is_red_node(self):
        return self.color == "R"

    def set_black_node(self):
        self.color = "B"

    def set_red_node(self):
        self.color = "R"

    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()


class RBTree:
    def __init__(self):
        self.root = None  # 根结点
        self.index = -1  # 当前产生图像位置
        self.action = ""
        self.snapshot()

    def snapshot(self):
        self.index += 1
        save_tree(self.root, "{}".format(self.index))

    def left_rotate(self, node):
        parent = node.parent
        right = node.right

        node.right = right.left
        if node.right:
            node.right.parent = node

        right.left = node
        node.parent = right

        right.parent = parent
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right
        pass

    def right_rotate(self, node):
        parent = node.parent
        left = node.left

        node.left = left.right
        if node.left:
            node.left.parent = node

        left.right = node
        node.parent = left

        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left
        pass

    def search_node(self, val):
        if not self.root:
            return False

        cur = self.root
        while cur:
            if cur.val == val:
                return True

            if cur.val < val:
                if not cur.right:
                    return False
                cur = cur.right
                continue

            if cur.val > val:
                if not cur.left:
                    return False
                cur = cur.left
                continue
        return False

    def insert_node(self, node):
        if not self.root:
            self.root = node
            return True

        cur = self.root
        while cur:
            if cur.val < node.val:
                if not cur.right:
                    node.parent = cur
                    cur.right = node
                    return True
                cur = cur.right
                continue

            if cur.val > node.val:
                if not cur.left:
                    node.parent = cur
                    cur.left = node
                    return True
                cur = cur.left
                continue

            if cur.val == node.val:
                return False
        pass

    def check_node(self, node):
        if self.root == node:
            self.root.set_black_node()
            self.snapshot()
            return

        if self.root == node.parent:
            self.root.set_black_node()
            return

        if node.parent.is_black_node():
            return

        grand = node.parent.parent
        if not grand:
            self.check_node(node.parent)
            return
        if grand.left and grand.left.is_red_node() \
                and grand.right and grand.right.is_red_node():
            grand.left.set_black_node()
            grand.right.set_black_node()
            grand.set_red_node()
            self.snapshot()
            self.check_node(grand)
            return

        parent = node.parent
        if parent.left == node and grand.right == node.parent:
            self.right_rotate(node.parent)
            self.snapshot()
            self.check_node(parent)
            return
        if parent.right == node and grand.left == node.parent:
            parent = node.parent
            self.left_rotate(node.parent)
            self.snapshot()
            self.check_node(parent)
            return

        parent.set_black_node()
        grand.set_red_node()
        if parent.left == node and grand.left == node.parent:
            self.right_rotate(grand)
            self.snapshot()
            return
        if parent.right == node and grand.right == node.parent:
            self.left_rotate(grand)
            self.snapshot()
            return
        self.snapshot()

    def add_node(self, node):
        self.action = 'insert node {}'.format(node.val)
        if self.insert_node(node):
            self.snapshot()
            self.check_node(node)
        pass

    def check_delete_node(self, node):
        if self.root == node or node.is_red_node():
            return

        node_is_left = node.parent.left == node
        brother = node.parent.right if node_is_left else node.parent.left
        if brother.is_red_node():
            if node_is_left:
                self.left_rotate(node.parent)
            else:
                self.right_rotate(node.parent)
            self.snapshot()
            node.parent.set_red_node()
            brother.set_black_node()
            self.snapshot()
            print("check node delete more ")
            self.check_delete_node(node)
            return

        all_none = not brother.left and not brother.right
        all_black = brother.left and brother.right \
            and brother.left.is_black_node(
            ) and brother.right.is_black_node()
        if all_none or all_black:
            brother.set_red_node()
            if node.parent.is_red_node():
                node.parent.set_black_node()
                self.snapshot()
                return
            self.check_delete_node(node.parent)
            return

        brother_same_right_red = node_is_left \
            and brother.right and brother.right.is_red_node()
        brother_same_left_red = not node_is_left \
            and brother.left and brother.left.is_red_node()
        if brother_same_right_red or brother_same_left_red:
            if node.parent.is_red_node():
                brother.set_red_node()
            else:
                brother.set_black_node()
            node.parent.set_black_node()

            if brother_same_right_red:
                brother.right.set_black_node()
                self.left_rotate(node.parent)
            else:
                brother.left.set_black_node()
                self.right_rotate(node.parent)
            self.snapshot()
            return True

        brother_diff_right_red = not node_is_left \
            and brother.right and brother.right.is_red_node()
        brother_diff_left_red = node_is_left \
            and brother.left and brother.left.is_red_node()
        if brother_diff_right_red or brother_diff_left_red:
            brother.set_red_node()
            if brother_diff_right_red:
                brother.right.set_black_node()
                self.left_rotate(brother)
            else:
                brother.left.set_black_node()
                self.right_rotate(brother)
            self.snapshot()
            self.check_delete_node(node)
            return True

    def pre_delete_node(self, node):
        post_node = self.get_post_node(node)
        if post_node:
            node.val, post_node.val = post_node.val, node.val
            self.snapshot()
            return self.pre_delete_node(post_node)
        pre_node = self.get_pre_node(node)
        if pre_node:
            pre_node.val, node.val = node.val, pre_node.val
            self.snapshot()
            return self.pre_delete_node(pre_node)
        return node

    def get_pre_node(self, node):
        if not node.left:
            return None
        pre_node = node.left
        while pre_node.right:
            pre_node = pre_node.right
        return pre_node

    def get_post_node(self, node):
        if not node.right:
            return None
        post_node = node.right
        while post_node.left:
            post_node = post_node.left
        return post_node

    def get_node(self, val):
        if not self.root:
            return None
        node = self.root
        while node:
            if node.val == val:
                break
            if node.val > val:
                node = node.left
                continue
            else:
                node = node.right
        return node

    def delete_node(self, val):
        node = self.get_node(val)
        if not node:
            print("node error {}".format(val))
            return
        node = self.pre_delete_node(node)
        self.check_delete_node(node)
        self.real_delete_node(node)
        pass

    def real_delete_node(self, node):
        if self.root == node:
            self.root = None
            self.snapshot()
            return
        if node.parent.left == node:
            node.parent.left = None
            self.snapshot()
            return
        if node.parent.right == node:
            node.parent.right = None
            self.snapshot()
        return
