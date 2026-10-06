class TimeMap:

    def __init__(self):
        self.keyValStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValStore:
            self.keyValStore[key] = [""] * (timestamp)
            self.keyValStore[key].append(value)
        
        else:
            for i in range(timestamp - len(self.keyValStore[key])):
                self.keyValStore[key].append(self.keyValStore[key][-1])
            
            self.keyValStore[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyValStore:
            return ""

        elif timestamp > len(self.keyValStore[key]) - 1:
            return self.keyValStore[key][-1]
        
        else:
            return self.keyValStore[key][timestamp]