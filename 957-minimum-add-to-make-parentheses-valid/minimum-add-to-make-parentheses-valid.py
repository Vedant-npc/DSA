class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        ans = 0 

        for ch in s:
            if ch =='(':
                stack.append(ch)

            else:
                if stack:
                    stack.pop()
                else:
                    ans +=1

        return ans + len(stack)
        