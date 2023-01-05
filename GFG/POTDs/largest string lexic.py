class Solution():
    def longestString(self, arr, n):
        #your code goes here
        arr.sort(key=len)
        d={''}
        for s in arr:
            if s[:-1] in d:
                d.add(s)
        m=min(d,key=lambda x: (-(len(x)),x))
        return m
