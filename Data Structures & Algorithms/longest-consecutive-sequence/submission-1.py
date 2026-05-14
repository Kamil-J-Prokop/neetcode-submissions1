class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if num - 1 not in numbers:
                current = num
                length = 1

                while current + 1 in numbers:
                    current += 1
                    length += 1
                
                longest = max(longest, length)

        return longest

"""
#first try
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        output = 1 
        for num in nums:
            numbers.add(num)

        for num in numbers:
            if num - 1 not in numbers:
                output_candidate = 1
                for num in numbers:
                    if num+1 in numbers:
                        output_candidate +=1
                if output_candidate > output:
                    output = output_candidate

        return output
"""
