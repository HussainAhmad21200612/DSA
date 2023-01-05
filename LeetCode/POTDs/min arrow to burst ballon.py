class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        def fun(a):
            return a[1]
        points.sort(key=fun)
        print(points)
        end_point=points[0][1]
        ans=1
        for i in range(1,len(points)):
            if points[i][0]>end_point:
                ans+=1
                end_point=points[i][1]
        return ans
