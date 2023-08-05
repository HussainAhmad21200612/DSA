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

#Another solution
class Solution:
    def minimumDeviation(self, nums):
        upper_odd = 1
        lower = 1000000000
        for num in nums:
            upper_odd = max(upper_odd, num // (num & (-num)))
            lower = min(lower, num << (num & 1))
        lower = min(lower, upper_odd)
        lower2 = lower << 1
        if lower2 <= upper_odd:
            return upper_odd - lower
        arr = [upper_odd]
        for num in nums:
            a = num << 1
            while a >= lower2:
                a >>= 1
            if a > upper_odd:
                arr.append(a)
        arr.sort()
        div = arr[-1] - lower
        for i in range(len(arr) - 1, 0, -1):
            div = min(div, arr[i-1] - (arr[i] >> 1))
        return div

    def print_arr(self, nums):
        for num in nums:
            print(num, end=", ")
        print()

