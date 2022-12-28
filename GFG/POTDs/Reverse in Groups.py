class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		s=[]
		c=0
		for i in range(0,N,K):
		    if (i+K)<N:
		        arr[i:i+K]=arr[i:i+K][::-1]
		    else:
		        arr[i:]=arr[i:][::-1]
		return arr
		    
