class Solution:
    def trap(self, height: List[int]) -> int:
        le=len(height)
        left=[height[0]]
        right=[0]*(le-1)
        right.append(height[le-1])
        for i in range(1,le):
            left.append(max(left[i-1],height[i]))
        for i in range(le-2,-1,-1):
            right[i]=(max(right[i+1],height[i]))
        for i in range(le):
            left[i]=min(left[i],right[i])-height[i]
        return sum(left)
