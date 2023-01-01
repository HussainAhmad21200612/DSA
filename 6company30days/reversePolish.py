class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ll=['+','*','/','-']
        stack=[]
        res=0
        num1=-1
        num2=-1
        if len(tokens)==1:
            return int(tokens.pop())
        for i in tokens:
            if i in ll:
                num2=stack.pop()
                num1=stack.pop()
                if i=="+":
                    res=int(num1)+int(num2)
                elif i=="*":
                    res=int(num1)*int(num2)
                elif i=="/":
                    if int(num1)<0 and int(num2)<0:
                        num1=-1*int(num1)
                        num2=-1*int(num2)
                        res=num1//num2
                        
                    elif int(num2)<0:
                        num2=-1*int(num2)
                        res=int(num1)//num2
                        res*=-1
                    elif int(num1)<0:
                        num1=-1*int(num1)
                        res=num1//int(num2)
                        res*=-1
                    else:
                        res=int(num1)//int(num2)
                elif i=="-":
                    res=int(num1)-int(num2)
                stack.append(res)
            else:
                stack.append(i)
        return stack.pop()
