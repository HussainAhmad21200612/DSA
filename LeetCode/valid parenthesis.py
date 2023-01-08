class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i=='(':
                stack.append(')')
            elif i=='{':
                stack.append('}')
            elif i=='[':
                stack.append(']')
            elif len(stack)!=0 and stack[-1]==i:
                stack.pop()
            else:
                return False
        return (len(stack)==0)
