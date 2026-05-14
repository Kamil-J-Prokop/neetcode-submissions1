class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_array = [1] * len(nums)
        suffix_array = [1] * len(nums)
        output = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(1, len(nums)):
            prefix = prefix * nums[i - 1] 
            prefix_array[i] = prefix
        #print(prefix_array)

        for i in range(len(nums)- 2, -1, -1):
            suffix = suffix * nums[i + 1]
            suffix_array[i] = suffix
        
        
        #print("Prefix array:")
        #print(prefix_array)
        #print("Suffix array:")
        #print(suffix_array)

        output = [p * s for p, s in zip(prefix_array, suffix_array)]

        return output


"""
#Super clean solution from gpt:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output

"""