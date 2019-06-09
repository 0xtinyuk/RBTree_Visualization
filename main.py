#!/usr/bin/python3
import tkinter
from PIL import Image, ImageTk
import functools
import rbtree
import bstree
import time

root = tkinter.Tk()
tree = rbtree.RBTree()
index_displayed = -1


def load_img():
    global root, frame1, label_img, tree, index_displayed
    if index_displayed+1 > tree.index:
        return
    index_displayed += 1
    baseheight = 400
    img = Image.open('pics/output{}.png'.format(index_displayed))
    root.title('红黑树演示程序 第{}/{}步'.format(index_displayed, tree.index))
    print('printing pics/output{}.png'.format(index_displayed))
    hpercent = (baseheight/float(img.size[1]))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize, baseheight), Image.ANTIALIAS)
    img_png = ImageTk.PhotoImage(img)
    label_img.configure(image=img_png)
    label_img.image = img_png


def load_last_img():
    global root, frame1, label_img, tree, index_displayed
    if index_displayed-1 <= 0:
        return
    index_displayed -= 1
    baseheight = 400
    img = Image.open('pics/output{}.png'.format(index_displayed))
    root.title('红黑树演示程序 第{}/{}步'.format(index_displayed, tree.index))
    print('displaying pics/output{}.png'.format(index_displayed))
    hpercent = (baseheight/float(img.size[1]))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize, baseheight), Image.ANTIALIAS)
    img_png = ImageTk.PhotoImage(img)
    label_img.configure(image=img_png)
    label_img.image = img_png


def next_img(event):
    load_img()


def last_img(event):
    load_last_img()


def keep_loading_img():
    global index_displayed, tree
    if index_displayed > tree.index:
        index_displayed = -1
        load_img()
        return
    if index_displayed+1 <= tree.index:
        load_img()
        if index_displayed+1 <= tree.index:
            root.after(2000, keep_loading_img)


def insert_node(event):
    global e1, tree, index_displayed
    val = int(e1.get())
    keep_loading_img()
    if type(tree) == rbtree.RBTree:
        tree.add_node(rbtree.RBTreeNode(val, "R"))
    else:
        tree.add_node(bstree.BSTreeNode(val, "B"))
    e1.delete(0, 'end')
    keep_loading_img()
    pass


def delete_node(event):
    global e1, tree
    val = int(e1.get())
    keep_loading_img()
    tree.delete_node(val)
    e1.delete(0, 'end')
    keep_loading_img()
    pass


def search_node(event):
    global e1, tree
    val = int(e1.get())
    keep_loading_img()
    if tree.search_node(val):
        tkinter.messagebox.showinfo('查找结果', '{}存在'.format(val))
    else:
        tkinter.messagebox.showinfo('查找结果', '{}不存在'.format(val))
    e1.delete(0, 'end')
    pass


def switch_tree(event):
    global tree, b_switch_tree
    if type(tree) == rbtree.RBTree:
        tree = bstree.BSTree()
        b_switch_tree.config(text="新建红黑树")
        b_pre_order.config(state=tkinter.NORMAL)
        b_in_order.config(state=tkinter.NORMAL)
        b_post_order.config(state=tkinter.NORMAL)
    else:
        tree = rbtree.RBTree()
        b_switch_tree.config(text="新建二叉搜索树")
        b_pre_order.config(state=tkinter.DISABLED)
        b_in_order.config(state=tkinter.DISABLED)
        b_post_order.config(state=tkinter.DISABLED)
    keep_loading_img()
    pass


def pre_order_traversal(event):
    global tree
    if type(tree) == rbtree.RBTree:
        return

    result = tree.pre_order_traversal(tree.root)
    tree.snapshot()
    tkinter.messagebox.showinfo('遍历结果', '遍历顺序为{}'.format(result))
    keep_loading_img()
    pass


def in_order_traversal(event):
    global tree
    if type(tree) == rbtree.RBTree:
        return

    result = tree.in_order_traversal(tree.root)
    tree.snapshot()
    tkinter.messagebox.showinfo('遍历结果', '遍历顺序为{}'.format(result))
    keep_loading_img()
    pass


def post_order_traversal(event):
    global tree
    if type(tree) == rbtree.RBTree:
        return

    result = tree.post_order_traversal(tree.root)
    tree.snapshot()
    tkinter.messagebox.showinfo('遍历结果', '遍历顺序为{}'.format(result))
    keep_loading_img()
    pass


root.title('树形结构演示系统')
root.resizable(True, True)
root.geometry("")
root.wm_attributes('-topmost', 1)  # 将窗口置于最前
root.after(1000, lambda: root.attributes("-topmost", 0))  # 1秒后取消窗口置于最前，避免挡住弹窗

frame1 = tkinter.Frame(root, bd=2, relief='solid')
label_img = tkinter.Label(frame1)
label_img.pack(expand=1)
frame2 = tkinter.Frame(root, relief='solid')
b_switch_tree = tkinter.Button(frame2, text="新建二叉搜索树")
b_pre_order = tkinter.Button(frame2, text="前序遍历")
b_in_order = tkinter.Button(frame2, text="中序遍历")
b_post_order = tkinter.Button(frame2, text="后序遍历")
e1 = tkinter.Entry(frame2, width=10, justify=tkinter.RIGHT)
b0 = tkinter.Button(frame2, text="查找")
b1 = tkinter.Button(frame2, text="插入")
b2 = tkinter.Button(frame2, text="删除")
b3 = tkinter.Button(frame2, text="下一步")
b4 = tkinter.Button(frame2, text="上一步")
b_switch_tree.bind("<Button-1>", switch_tree)
b_pre_order.bind("<Button-1>", pre_order_traversal)
b_in_order.bind("<Button-1>", in_order_traversal)
b_post_order.bind("<Button-1>", post_order_traversal)
b0.bind("<Button-1>", search_node)
b1.bind("<Button-1>", insert_node)
b2.bind("<Button-1>", delete_node)
b3.bind("<Button-1>", next_img)
b4.bind("<Button-1>", last_img)

frame1.grid(row=0)
frame2.grid(row=1)
b_switch_tree.pack(side=tkinter.LEFT, fill=tkinter.X)
e1.pack(side=tkinter.LEFT)
b_post_order.pack(side=tkinter.RIGHT)
b_post_order.config(state=tkinter.DISABLED)
b_in_order.pack(side=tkinter.RIGHT)
b_in_order.config(state=tkinter.DISABLED)
b_pre_order.pack(side=tkinter.RIGHT)
b_pre_order.config(state=tkinter.DISABLED)
b3.pack(side=tkinter.RIGHT)
b4.pack(side=tkinter.RIGHT)
b2.pack(side=tkinter.RIGHT)
b1.pack(side=tkinter.RIGHT)
b0.pack(side=tkinter.RIGHT)

frame1.grid_propagate(False)
load_img()
root.mainloop()
