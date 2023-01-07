class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here 
		a=[0]*(2*n)
		i=0
		j=0
		k=0
		while(i<n and j<n):
		    if ar1[i]<ar2[j]:
		        a[k]=ar1[i]
		        i+=1
		        k+=1
		    else:
		        a[k]=ar2[j]
		        j+=1
		        k+=1
		while(i<n):
		    a[k]=ar1[i]
		    i+=1
		    k+=1
		while(j<n):
		    a[k]=ar2[j]
		    j+=1
		    k+=1

		return a[k//2-1]+a[k//2] 
