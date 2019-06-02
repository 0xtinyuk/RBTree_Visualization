import tkinter
from PIL import Image, ImageTk
import functools
import rbtree
import time

root = tkinter.Tk()
manager = []
tree = rbtree.RBTree()
index_displayed = 0


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
    if index_displayed+1 <= tree.index:
        load_img()
        if index_displayed+1 <= tree.index:
            root.after(2000, keep_loading_img)


def insert_node(event):
    global e1, tree, index_displayed
    val = int(e1.get())
    keep_loading_img()
    tree.add_node(rbtree.RBTreeNode(val))
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


root.title('红黑树演示程序')
root.resizable(True, True)
root.geometry("")
root.wm_attributes('-topmost', 1)

frame1 = tkinter.Frame(root, bd=2, relief='solid')
label_img = tkinter.Label(frame1)
label_img.pack(expand=1)
frame2 = tkinter.Frame(root, relief='solid')
e1 = tkinter.Entry(frame2, width=10, justify=tkinter.RIGHT)
b1 = tkinter.Button(frame2, text="插入")
b2 = tkinter.Button(frame2, text="删除")
b3 = tkinter.Button(frame2, text="下一步")
b4 = tkinter.Button(frame2, text="上一步")
b1.bind("<Button-1>", insert_node)
b2.bind("<Button-1>", delete_node)
b3.bind("<Button-1>", next_img)
b4.bind("<Button-1>", last_img)

frame1.grid(row=0)  
frame2.grid(row=1)
e1.pack(side=tkinter.LEFT, fill=tkinter.X)  
b3.pack(side=tkinter.RIGHT)
b4.pack(side=tkinter.RIGHT)
b2.pack(side=tkinter.RIGHT)
b1.pack(side=tkinter.RIGHT)

frame1.grid_propagate(False)
manager.extend([frame1, label_img, e1, b1, b2, b3])
root.mainloop()

