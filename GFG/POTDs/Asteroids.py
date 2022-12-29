def asteroidCollision(self, N, asteroids):
        # Code here
        stack=[]
        for i in asteroids:
            if i<0:
                while(len(stack)!=0 and stack[len(stack)-1]>0 and stack[len(stack)-1]<abs(i)):
                    stack.pop()
                if len(stack)!=0:
                    if stack[len(stack)-1]==abs(i):
                        stack.pop()
                    elif stack[len(stack)-1]<0:
                        stack.append(i)
                else:
                    stack.append(i)
                
            else:
                stack.append(i)
 
        return stack
