class Solution:
    # Your task is to complete this function
    def ExtremeNodes(self, root):
        # Code here
        def newNode( data):
 
            temp = Node(0)
            temp.data = data
            temp.left = temp.right = None
            return temp
 
        # Function to print nodes of extreme corners
        # of each level in alternate order
        def printExtremeNodes( root):
         
            if (root == None):
                return
         
            # Create a queue and enqueue left and right
            # children of root
            q = []
            q.append(root)
            flag = False
            while (len(q) > 0):
                nodeCount = len(q)
                n = nodeCount
                while (n > 0):
                    n = n - 1
                    curr = q[0]
         
                    # Enqueue left child
                    if (curr.left != None):
                        q.append(curr.left)
                    if (curr.right != None):
                        q.append(curr.right)
                    q.pop(0)
                    if (flag and n == nodeCount - 1):
                        print( curr.data , end=" ")
                    if (not flag and n == 0):
                        print( curr.data ,end= " ")
                flag = not flag
        printExtremeNodes(root)
        return []
