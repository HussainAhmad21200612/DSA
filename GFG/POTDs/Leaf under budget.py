from queue import Queue

class Solution:
    def getCount(self, root, k):
        ans = 0
        q = Queue()
        q.put((root, 1))
        while not q.empty():
            cur, level = q.get()
            if cur.left is not None:
                q.put((cur.left, level + 1))
            if cur.right is not None:
                q.put((cur.right, level + 1))
            if cur.left is None and cur.right is None:
                if level <= k:
                    k -= level
                    ans += 1
        return ans
