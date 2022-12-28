import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        ll=[]
        for i in piles:
            heapq.heappush(ll,-i)
        
        while(k>0):
            curr=-heapq.heappop(ll)
            curr-=curr//2
            heapq.heappush(ll,-curr)
            k-=1
        return -sum(ll)
        
