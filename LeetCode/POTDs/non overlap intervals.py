class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def fun(a):
            return a[1]
        intervals.sort(key=fun)
        end=-10000000000
        ans=0
        for i in range(len(intervals)):
            if intervals[i][0]<end:
                ans+=1
            else:
                end=intervals[i][1]
        return ans
