class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict_s = dict()
        char_dict_t = dict()
        if len(s) != len(t):
            return False
        elif len(s) == 0 and len(t) == 0:
            return True
        for ch in s:
            if ch not in char_dict_s:
                char_dict_s[ch] = 1
            else:
                char_dict_s[ch] += 1
        for ch in t:
            if ch not in char_dict_t:
                char_dict_t[ch] = 1
            else:
                char_dict_t[ch] += 1
        if char_dict_s == char_dict_t:
            return True
        else:
            return False