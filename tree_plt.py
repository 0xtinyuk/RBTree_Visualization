import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np


def get_height(node):
    if not node:
        return 0
    return 1 + max([get_height(node.left), get_height(node.right)])


def get_node_count(node):
    if not node:
        return 0
    return 1 + get_node_count(node.left) + get_node_count(node.right)


def get_fontsize(count):
    if count < 10:
        return 30
    if count < 20:
        return 20
    return 16


def show_node(node, ax, height, index, font_size=12):
    if not node:
        return
    x1, y1 = None, None
    if node.left:
        x1, y1, index = show_node(node.left, ax, height-1, index, font_size)
    x = 100 * index - 50
    y = 100 * height - 50
    if x1:
        plt.plot((x1, x), (y1, y), linewidth=2.0, color='b')
    circle_color = "black" if node.is_black_node() else 'r'
    text_color = "beige" if node.is_black_node() else 'black'
    ax.add_artist(plt.Circle((x, y), 50, color=circle_color))
    ax.add_artist(plt.Text(x, y, node.val, color=text_color, fontsize=font_size,
                           horizontalalignment="center", verticalalignment="center"))

    index += 1
    if node.right:
        x1, y1, index = show_node(node.right, ax, height-1, index, font_size)
        plt.plot((x1, x), (y1, y), linewidth=2.0, color='b')

    return x, y, index


def save_tree(tree, index):
    fig, ax = plt.subplots()
    fig.set_facecolor('gray')
    height = get_height(tree)
    h = height*100+100
    w = 100 * get_node_count(tree) + 100
    plt.ylim(0, h)
    plt.xlim(0, w)
    plt.axis('off')
    show_node(tree, ax, height, 1, get_fontsize(get_node_count(tree)))
    fig.set_size_inches(10, h/(w/10))
    plt.savefig("pics/output{}.png".format(index))
    print("pics/output{}.png".format(index))
