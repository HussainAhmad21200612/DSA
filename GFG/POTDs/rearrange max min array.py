class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        '''for i in range(0,n,2):
            arr.insert(i,arr.pop())
        '''
        ll=[]
        l=0
        h=n-1
        for i in range(n):
            if i%2==0:
                ll.append(arr[h])
                h-=1
            else:
                ll.append(arr[l])
                l+=1
        arr[::]=ll
