class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # signals is warmer day future, first day warmer, need to track current temp/past temps/and when warmer temp comes meaning track index by window
        # pattern stack because you need to know the day soonest warmer temp comes
        # brute force compare every single temp to next temps and find the soonest warmer day

        output = [0] * len(temperatures)

        stack = []
        left = 0

        for idx in range(len(temperatures)):
            current_temp = temperatures[idx]

            # i cant really figure out how the logic works when you skip days i get that like on day 2 temp 38 and day 5 temp 40 so idx 5 - 1 is 4 so 4 days
            # i guess you could push both temp and idx to stack and compare both but feels infficient
            while stack and temperatures[stack[-1]] < current_temp:
                output[stack[-1]] = idx - stack[-1]
                stack.pop()
            # you push index and then on warmer temp you subtract latest day index to previous index in stack and pop
            stack.append(idx)
        
        return output
        
        