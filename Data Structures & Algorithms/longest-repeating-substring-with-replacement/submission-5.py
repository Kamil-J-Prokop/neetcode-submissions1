class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0  #left pointer
        longest_substring = 0
        counts = {}

        for i, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1

            while ((i - l + 1) - max(counts.values())) > k:
                counts[s[l]] = counts.get(s[l], 0) - 1
                l += 1


            longest_substring = max(longest_substring, i - l + 1)

        return longest_substring

