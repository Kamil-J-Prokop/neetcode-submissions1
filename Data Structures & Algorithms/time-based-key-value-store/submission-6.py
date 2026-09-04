class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.storage:
            self.storage[key] = []
        
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""

        history = self.storage[key]
        l = 0
        r = len(history) - 1
        answer = ""

        while l <= r:
            m = l + (r - l) // 2

            if history[m][0] <= timestamp:
                answer = history[m][1]
                l = m + 1
            else:
                r = m - 1

        return answer
            

        
