class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        tracker = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                # i need the char count to be the key
                # value is the an array of the words with that char count
                count[index] += 1
            
            key = tuple(count)
            if key in tracker:
                tracker[key].append(word)
            else:
                tracker[key] = [word]
        

        all_values = list(tracker.values())
        return all_values