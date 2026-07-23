class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ["+", "*", "-", "/"]

        stack = []

        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "-":
                    stack.append(a - b)
                else:
                    stack.append(int(a / b))
        
        return int(stack[-1])
        