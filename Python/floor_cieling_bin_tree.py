"                   Shree Krishnaya Namaha         "

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    """ Find the ceil and floor in a BST"""
    floor = float("inf")
    ceil = float("-inf")
    cur_node = root_node

    cur_node = root_node
    while cur_node:
        if cur_node.value == k:
            ceil = cur_node.value
            floor = ceil
        if k < cur_node.value:
            ceil = cur_node.value
            cur_node = cur_node.left
        elif k > cur_node.value:
            floor = cur_node.value
            cur_node = cur_node.right
        else:
            break
    floor = floor if floor != float("inf") else None
    ceil = ceil if ceil != float("-inf") else None
    return (floor, ceil)
    

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print (findCeilingFloor(root, 5))