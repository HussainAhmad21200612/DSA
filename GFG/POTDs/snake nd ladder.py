class Solution:
    def minThrow(self, N, arr):
        # code here
        from typing import List, Dict
         
         
        def min_throw(n, arr) -> int:
            t = [-1] * 31
            h = {}
            for i in range(0, 2 * n, 2):
                h[arr[i]] = arr[i + 1]
            return sol(1, h, t)
         
         
        def sol(i, h, t) -> int:
            # base condition
            if i >= 30:
                return 0
            elif t[i] != -1:
                return t[i]
            min_value = float("inf")
            for j in range(1, 7):
                k = i + j
                if k in h:
                    if h[k] < k:
                        continue
                    k = h[k]
                min_value = min(min_value, sol(k, h, t) + 1)
            t[i] = min_value
            return t[i]
        return min_throw(N,arr)
