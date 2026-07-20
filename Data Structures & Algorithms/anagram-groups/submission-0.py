class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can sort the strings or do the grouping by char count

        result = {}
        final = []

        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            
            key = tuple(count)

            if key not in result:
                result[key] = [word]
            else:
                result[key].append(word)
        
        for key, value in result.items():
            final.append(value)
        
        return final