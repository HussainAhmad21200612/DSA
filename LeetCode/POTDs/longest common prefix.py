
class Solution:
    def longestCommonPrefix(self, arr, n):
        l=[]
        for i in arr:
            l.append(len(i))
        minimum=min(l)
        ind=l.index(min(l))
        base=arr[ind]
        output=""
        s=""
        for i in range(0,minimum):
            s=s+base[i]
            nl=list(filter(lambda x:x.startswith(s),arr))
            if nl==arr:
                output=s 

            else:
                break 
        if output=="":
            return -1
        
        return output 
