class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        if len(nums1)>len(nums2):
            new_n=nums2.copy()
            new_n2=nums1.copy()
            n=len(new_n)
        else:
            
            new_n=nums1.copy()
            new_n2=nums2.copy()
            n=len(new_n)
        for i in range(n):
            if new_n[i] in new_n2:
                ans.append(new_n[i])
                new_n2.remove(new_n[i])
        return ans
