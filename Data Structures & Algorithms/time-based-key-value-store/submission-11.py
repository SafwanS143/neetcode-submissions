class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[timestamp, value]]

        else:
            self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        left = 0
        right = len(self.store[key])

        while left < right:
            mid = (right + left) // 2

            if self.store[key][mid][0] > timestamp:
                right = mid
            
            else:
                left = mid + 1

        return self.store[key][left - 1][1] if left > 0 else ""