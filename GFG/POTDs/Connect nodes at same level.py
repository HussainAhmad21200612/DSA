class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        

            if root is None:
                return
         
            # Create an empty queue like level order traversal
            queue = []
            queue.append(root)
            while len(queue) != 0:
         
                # size indicates no. of nodes at current level
                size = len(queue)
         
                # for keeping track of previous node
                prev = Node(None)
                for i in range(size):
                    temp = queue.pop(0)
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
                    if prev != None:
                        prev.nextRight = temp
                        prev = temp
                prev.nextRight = None
