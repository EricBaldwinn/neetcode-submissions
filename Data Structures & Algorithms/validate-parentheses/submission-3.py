class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for symbol in s:
            if stack and symbol in key:
                pop = stack.pop()
                if key[symbol] != pop:
                    return False
            else:
                stack.append(symbol)

        return len(stack) == 0  
        