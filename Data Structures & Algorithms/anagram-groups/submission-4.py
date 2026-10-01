class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            key = tuple(count)
            if key in tracker:
                tracker[key].append(word)
            else:
                tracker[key] = [word]
        
        return list(tracker.values())

        