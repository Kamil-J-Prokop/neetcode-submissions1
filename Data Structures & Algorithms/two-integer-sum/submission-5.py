class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            sum_target = target - nums[left]
            intermediate_pointer = left + 1
            while intermediate_pointer <= right:
                if nums[intermediate_pointer] == sum_target:
                    return [left, intermediate_pointer]
                else:
                    intermediate_pointer += 1

            left += 1
            
        return None