    def leaders(self, A, N):
        #Code here
        max1=-1
        ll=[]
        for i in range(N-1,-1,-1):
            if A[i]>=max1:
                ll.append(A[i])
                max1=A[i]
        return ll[::-1]
