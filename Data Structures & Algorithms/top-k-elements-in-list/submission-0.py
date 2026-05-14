class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = {}

        for element in nums:
            if element in frequency_count:
                frequency_count[element] += 1
            else:
                frequency_count[element] = 1

        output = []

        while k > 0:
            current_max_val = max(frequency_count, key=frequency_count.get)
            if frequency_count:
                output.append(current_max_val)
            else:
                output.append(None)
            k -= 1
            frequency_count.pop(current_max_val)
            
        return output
        

