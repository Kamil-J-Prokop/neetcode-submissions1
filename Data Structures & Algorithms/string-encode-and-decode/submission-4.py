class Solution:

    
    def encode(self, strs: List[str]) -> str:
        """
        output =""
        for item in strs:
            output += str(len(item))
            output += "#"
            output += item
        return output
        """
    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        output = []
        chars_to_read = 0
        number_str = ""
        temp_output = ""
        for ch in s:
            if "0" <= ch <= "9" and chars_to_read == 0:
                number_str += ch
                continue
            if ch == "#" and chars_to_read == 0:
                chars_to_read = int(number_str)
                if chars_to_read == 0:
                    output.append("")
                number_str = ""
                continue
            temp_output += ch
            chars_to_read -= 1
            if chars_to_read == 0:
                output.append(temp_output)
                temp_output = ""
        return output

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            output.append(s[start:end])
            i = end

        return output

"""
