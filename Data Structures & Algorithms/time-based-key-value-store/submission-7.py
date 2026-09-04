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
        left = 0
        right = len(history) - 1
        answer = ""

        while left <= right:
            mid = left + (right - left) // 2

            if history[mid][0] <= timestamp:
                answer = history[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return answer
        
