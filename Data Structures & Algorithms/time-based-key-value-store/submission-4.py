class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[value, timestamp]]
        else:
            self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map[key]
        left = 0
        right = len(values) - 1
        result = ""
        # if key exists check for timestamp if not take lower timestamp
        while left <= right:
            mid = (right + left) // 2
            mid_value, mid_timestamp = values[mid]

            if mid_timestamp <= timestamp:
                result = mid_value
                left = mid + 1
            else:
                right = mid - 1
        
        return result



        
