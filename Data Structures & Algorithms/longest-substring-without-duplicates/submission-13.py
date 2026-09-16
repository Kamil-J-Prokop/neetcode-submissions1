class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        l, r = 0, 0
        seen_chars = set()

        while r < len(s):

            while s[r] in seen_chars:
                seen_chars.discard(s[l])
                l += 1
            
            seen_chars.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)
            
            r += 1
            
            

        
        return longest_substring
