class Solution:
    def maxSlidingWindow(self, arr: List[int], K: int) -> List[int]:
        from collections import deque
        q = deque()
        ans=[]
        N=len(arr)
        for i in range(K):
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
        for i in range(K, N):
            ans.append((arr[q[0]]))
            while q and q[0] <= i-K:
                q.popleft()
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
        ans.append(((arr[q[0]])))
        return ans
