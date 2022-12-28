class Solution:
    def nextPermutation(self, N, arr):
        # code here
        if N==0 or N==1:
            return
        i=N-1
        c=1
        for i in range(N-2,-1,-1):
            if arr[i]<arr[i+1]:
                c=0
                break
        if c==1:
            arr.reverse()
        else:
            for l in range(N-1,-1,-1):
                
                if arr[l]>arr[i]:
                    break
            arr[l],arr[i]=arr[i],arr[l]
            arr[i+1:]=arr[i+1:][::-1]
        return arr
      
      '''
      traverse from back and see where a[i]<a[i+1] like: 132 so 2<3 
      now if no such index ind1 exist just reverse
      else find ind2 s t a[ind1]<a[ind2]
      swap a[ind1],a[ind2]
      and reverse entire array after index1
      '''
