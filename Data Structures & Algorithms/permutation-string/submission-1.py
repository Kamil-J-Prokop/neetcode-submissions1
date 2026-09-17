class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapped_s1 = {}

        if len(s2) < len(s1):
            return False

        for ch in s1:
            if ch in mapped_s1:
                mapped_s1[ch] += 1
            else:
                mapped_s1[ch] = 1
        
        mapped_s2 = {}
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            temp_l = l
            while temp_l <= r:
                if s2[temp_l] in mapped_s2:
                    mapped_s2[s2[temp_l]] += 1
                else:
                    mapped_s2[s2[temp_l]] = 1
                temp_l += 1

            if mapped_s2 == mapped_s1:
                return True
            
            mapped_s2.clear()
            r += 1
            l += 1
        
        return False

