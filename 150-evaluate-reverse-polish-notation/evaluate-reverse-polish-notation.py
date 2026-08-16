class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for ch in tokens:
            if ch =='+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif ch =='-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif ch =='*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            
            elif ch =='/':
                b = stack.pop()
                a = stack.pop()
            
                if a * b < 0:
                    stack.append(-(abs(a) // abs(b)))
                else:
                    stack.append(abs(a) // abs(b))
            
            else:
                stack.append(int(ch))
            
        return stack[-1]
        