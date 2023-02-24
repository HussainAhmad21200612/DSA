class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap=[]
        mx=[]
        for i in nums:
            if i&1:
                # heapq.heappush(heap,i*2)
                heapq.heappush(mx,-i*2)
            else:
                # heapq.heappush(heap,i)
                heapq.heappush(mx,-i)
        # print(mx)
        mnn=-max(mx)
        diff=float('inf')
        while(len(nums)==len(mx)):
            # mn=heapq.heappop(heap)
            mxx=-heapq.heappop(mx)
            diff=min(diff,mxx-mnn)
            if mxx%2==0:
                mnn=min(mxx//2,mnn)
                heapq.heappush(mx,-mxx//2)
            else:
                break
            # print(mx,diff,mnn)
        return diff
