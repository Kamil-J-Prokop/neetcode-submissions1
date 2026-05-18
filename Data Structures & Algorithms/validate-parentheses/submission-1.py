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
