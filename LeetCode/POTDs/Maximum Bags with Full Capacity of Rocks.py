class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ll=[]
        for i in range(len(rocks)):
            ll.append(capacity[i]-rocks[i])
        ll.sort()
        c=0
        r=additionalRocks
        for i in ll:
            if i==0:
                c+=1
            elif i>0 and i<=r:
                c+=1
                r-=i
            else:
                if r==0:
                    break
        return c
