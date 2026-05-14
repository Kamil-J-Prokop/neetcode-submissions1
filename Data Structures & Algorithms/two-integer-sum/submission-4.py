class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        i = 0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = i
            else:
                nums_dict[num] = i
            i += 1

        i = 0

        for num in nums:
            difference = target - num

            if difference in nums_dict and i != nums_dict[difference] :
                return [i, nums_dict[difference]]
            i += 1

# trochę kurwa syf z tymi i w pętlach for i tym warunkiem w ostatnim ifie, trzeba by zrobić while aby miało to znamiona cywilizacji
            