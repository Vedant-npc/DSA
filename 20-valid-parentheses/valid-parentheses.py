class Solution(object):
    def isValid(self, s):
        stack = []

        for brackets in s:
            if brackets == '(' or brackets == '{' or brackets == '[':
                stack.append(brackets)

            else:
                if not stack:
                    return False

                if brackets == ')' and stack[-1] == '(':
                    stack.pop()

                elif brackets == '}' and stack[-1] == '{':
                    stack.pop()

                elif brackets == ']' and stack[-1] == '[':
                    stack.pop()

                else:
                    return False

        if stack:
            return False
        else:
            return True

            
        
        