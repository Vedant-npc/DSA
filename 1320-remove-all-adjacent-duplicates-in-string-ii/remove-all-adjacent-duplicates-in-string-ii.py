class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        count = []

        for ch in s:
            if stack and stack[-1] == ch:
                count[-1] += 1
            else:
                stack.append(ch)
                count.append(1)

            if count[-1] == k:
                stack.pop()
                count.pop()

        ans =""

        for i in range(len(stack)):
            ans += stack[i] * count[i]

        return ans