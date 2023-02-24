class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit=[]
        minCap=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minCap)
        for i in range(k):
            while minCap and minCap[0][0]<=w:
                a,b=heapq.heappop(minCap)
                heapq.heappush(maxProfit,-b)
            if not maxProfit:
                break
            w+=-1*heapq.heappop(maxProfit)
        return w
