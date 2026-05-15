class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        output = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                output.append(left+1)
                output.append(right+1)
                return output
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        return []