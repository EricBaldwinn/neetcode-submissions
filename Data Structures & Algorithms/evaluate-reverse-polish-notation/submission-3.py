class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        symbols = ["+", "*", "-", "/"]

        for symbol in tokens:
            if stack and symbol in symbols:
                b = stack.pop()
                a = stack.pop()
                if symbol == "+":
                    stack.append(a + b)
                elif symbol == "*":
                    stack.append(a * b)
                elif symbol == "-":
                    stack.append(a - b)
                else:
                    stack.append(int(a / b))
            else:
                symbol = int(symbol)
                stack.append(symbol)
        
        return stack[-1]

        