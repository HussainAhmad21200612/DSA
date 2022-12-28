import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        ts=sum(nums)/2
        c=0.0
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        i=0
        while(c<ts):
            i+=1
            cur=-heapq.heappop(heap)
            c+=cur/2
            heapq.heappush(heap,-cur/2)
        return i
