class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {"[", "{", "("}

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                elif stack[-1] == "[":
                    if bracket == "]":
                        stack.pop()
                    else:
                        return False
                elif stack[-1] == "{":
                    if bracket == "}":
                        stack.pop()
                    else:
                        return False
                elif stack[-1] == "(":
                    if bracket == ")":
                        stack.pop()
                    else:
                        return False

        if stack:
            return False

        return True

"""
#Dictionary based:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for bracket in s:
            if bracket in matching:
                if not stack or stack[-1] != matching[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)

        return not stack
    
"""
