"""         Shree Krishnaya Namaha      """

import sys
from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def preorder(self):
        #print (self.value)
        sys.stdout.write(str(self.value) + " ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

def invert(tree):
    """
    To invert a binary tree, we need to traverse the tree in-order
    and swap the left and right children at the current level.
    In order traversal is achieved using a FIFO 
    (implemented using deuque here, for better performance. You can use a list as well)
    """
    if tree is None:
        return

    nodes = deque()
    nodes.append(tree)

    while nodes:
        cur_node = nodes.popleft()    # Use deque for better perfomrance list.pop() is O(n)
        cur_node.left, cur_node.right = cur_node.right, cur_node.left
        if cur_node.left:
            nodes.append(cur_node.left)
        if cur_node.right:
            nodes.append(cur_node.right)


def main():
    """
    Test func to invert a tree.

    The tree:
                     a
                   /   \
                  b     c
                 / \   / \
                d   e  f
    """
    root = Node('a') 
    root.left = Node('b') 
    root.right = Node('c') 
    root.left.left = Node('d') 
    root.left.right = Node('e') 
    root.right.left = Node('f') 


    root.preorder()
    # a b d e c f 
    print ("")
    invert(root)
    root.preorder()
    # a c f b e d


if __name__ == "__main__":
    main()
