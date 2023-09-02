from queue import Queue
def maxNodeLevel(root):
    if (root == None):
        return -1
 
    q = Queue()
    q.put(root)
    level = 0
    Max = -999999999999
    level_no = 0
 
    while (1):
        NodeCount = q.qsize()
 
        if (NodeCount == 0):
            break
        if (NodeCount > Max):
            Max = NodeCount
            level_no = level
        while (NodeCount > 0):
            Node = q.queue[0]
            q.get()
            if (Node.left != None):
                q.put(Node.left)
            if (Node.right != None):
                q.put(Node.right)
            NodeCount -= 1
 
        level += 1
 
    return level_no
