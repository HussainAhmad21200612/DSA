def maxArea(A,le):
    #code here
    ar=0
    l=0
    h=le-1
    while(l<h):
        p=(h-l)*min(A[h],A[l])
        if A[l]<A[h]:
            l+=1
        else:
            h-=1
        ar=max(ar,p)
        
    return ar
