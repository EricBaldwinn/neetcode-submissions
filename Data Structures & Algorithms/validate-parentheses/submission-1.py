class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for symbol in s:
            if symbol in key:
                if not stack:
                    return False

                left = stack.pop()
                if key[symbol] != left:
                    return False
            else:
                stack.append(symbol)
            
        
        return len(stack) == 0

        