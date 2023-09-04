from typing import List

class Solution:
    
    def shortestPath(self,grid, source, destination):
        if source[0] == destination[0] and source[1] == destination[1]:
            return 0
        q = []
        n = len(grid)
        m = len(grid[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[source[0]][source[1]] = 0
        q.append((0, (source[0], source[1])))
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        while q:
            it = q.pop(0)
            dis = it[0]
            r = it[1][0]
            c = it[1][1]
            for i in range(4):
                newr = r + dr[i]
                newc = c + dc[i]
                if (newr >= 0 and newr < n and newc >= 0 and newc < m and grid[newr][newc] == 1 and dis + 1 < dist[newr][newc]):
                    dist[newr][newc] = 1 + dis
                    if (newr == destination[0] and newc == destination[1]):
                        return dis + 1
                    q.append((1 + dis, (newr, newc)))
        return -1
