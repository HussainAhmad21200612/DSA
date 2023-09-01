def printCorner(root):
    from collections import deque
    # print corner data, no need to print new line
    # code here
    if root == None:
        return
 
    # Do level order traversal
    # using a single queue
    q = deque()
    q.append(root)
 
    while q:
        n = len(q)
        for i in range(n):
            temp = q[0]
            q.popleft()
            if i == 0 or i == n - 1:
                print(temp.data, end = " ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
 
