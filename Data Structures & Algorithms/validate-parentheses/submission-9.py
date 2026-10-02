class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for symbol in s:
            if symbol not in key:
                stack.append(symbol)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if key[symbol] != opening:
                    return False
        return len(stack) == 0

        