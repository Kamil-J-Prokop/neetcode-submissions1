class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        i = 0
        j = len(cleaned) - 1
        while i <= j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1

        return True
