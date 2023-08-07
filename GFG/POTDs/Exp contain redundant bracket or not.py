class Solution():

    def checkRedundancy(self, s):
        st=[]
        op=['+','-','/','*']
        #your code goes here
        for i in s:
            if i==')':
                f=1
                t=st[-1]
                while(len(st)!=0 and t!="("):
                    if t in op:
                        f=0
                    t=st[-1]
                    st.pop()
                if f:
                    return 1
            else:
                st.append(i)
        return 0
