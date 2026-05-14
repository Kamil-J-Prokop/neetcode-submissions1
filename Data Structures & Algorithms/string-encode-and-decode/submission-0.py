class Solution:

    def encode(self, strs: List[str]) -> str:
        output =""
        for item in strs:
            output += str(len(item))
            output += "#"
            output += item
        return output

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




