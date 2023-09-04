from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0]*n for _ in range(n)]
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        q = deque([(0,0)])
        res = 0
        while q:
            m = len(q)
            for i in range(m):
                r,c = q.popleft()
                if r<0 or r>=n or c<0 or c>=n or grid[r][c]==1 or visited[r][c]:
                    continue
                if r==n-1 and c==n-1:
                    return res+1
                visited[r][c] = 1
                q.append((r-1,c-1))
                q.append((r-1,c))
                q.append((r-1,c+1))
                q.append((r,c-1))
                q.append((r,c+1))
                q.append((r+1,c-1))
                q.append((r+1,c))
                q.append((r+1,c+1))
            res+=1
        return -1
