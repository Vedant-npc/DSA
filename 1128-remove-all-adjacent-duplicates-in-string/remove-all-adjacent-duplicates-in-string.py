class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for words in s:
            if stack and words == stack[-1]:
                stack.pop()
            else:
                stack.append(words)

        return "".join(stack)
        