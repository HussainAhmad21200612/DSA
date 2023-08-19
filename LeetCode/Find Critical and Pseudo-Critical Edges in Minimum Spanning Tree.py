class DSU:
    def __init__(self, N):
        self.p = list(range(0,N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        def kruskal(n, edges, taken):
            dsu, ans = DSU(n), 0
            for x, y, w in taken: 
                dsu.union(x, y)
                ans += w
            for x, y, w in sorted(edges, key = lambda x:x[2]):
                if dsu.find(x) == dsu.find(y): continue
                dsu.union(x, y)
                ans += w
            return ans
        
        ans = [[], []]
        MST = kruskal(n, edges, [])
        for i, (x, y, w) in enumerate(edges):
            edges2 = edges[:]
            edges2.remove([x, y, w])
            MST1 = kruskal(n, edges2, [])
            MST2 = kruskal(n, edges2, [[x, y, w]])
            if MST2 == MST:
                ind = 1 if MST1 == MST else 0
                ans[ind].append(i)
           
        return ans
