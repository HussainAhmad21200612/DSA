import math
import collections
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count=collections.Counter()
        mod=10**9+7
        tot=0
        for i in deliciousness:
            for j in range(22):
                t=2**j-i
                if t in count:
                    tot+=count[t]
            count[i]+=1
        return tot%mod
