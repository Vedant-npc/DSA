class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = "+"
        for ch in s + '+':
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch != ' ':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)

                elif op == '*':
                    stack.append(stack.pop() * num)

                elif op == '/':
                    a = stack.pop()

                    if a < 0:
                        stack.append(-((-a) // num))
                    else:
                        stack.append(a // num)

                op = ch
                num = 0

        return sum(stack)   