class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        left = 0

        for right in range(len(temperatures)):
            while stack and temperatures[right] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                answer[previous_index] = right - previous_index
            
            stack.append(right)
        
        return answer

        