import sys
class Solution:
    def maxDistance (self, arr, n) : 
        #Complete the function
        mx_1=-sys.maxsize - 1 #arr[0]
        mx_2=-sys.maxsize - 1 #arr[0]
        mn_1=sys.maxsize #arr[0]
        mn_2=sys.maxsize #arr[0]
        for i in range(n):
            mx_1=max(mx_1,arr[i]-i)
            mn_1=min(mn_1,arr[i]-i)
            mx_2=max(mx_2,arr[i]+i)
            mn_2=min(mn_2,arr[i]+i)

        return max(mx_1-mn_1,mx_2-mn_2)
