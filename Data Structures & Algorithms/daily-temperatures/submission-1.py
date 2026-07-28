class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        monostack = []

        for idx in range(len(temperatures)):
            currenttemp = temperatures[idx]

            while monostack and currenttemp > temperatures[monostack[-1]]:
                output[monostack[-1]] = idx - monostack[-1]
                monostack.pop()

        
            monostack.append(idx)

        return output
        