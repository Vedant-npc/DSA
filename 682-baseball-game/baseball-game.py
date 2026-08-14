class Solution(object):
    def calPoints(self, operations):
        stack = []

        for ch in operations:
            if ch =="C":
                stack.pop()

            elif ch == "D":
                stack.append(stack[-1] * 2)

            elif ch == "+":
                stack.append(stack[-1] + stack[-2])
            
            else:
                stack.append(int(ch))

        count = 0
        while stack:
            count += stack[-1]
            stack.pop()

        return count



        