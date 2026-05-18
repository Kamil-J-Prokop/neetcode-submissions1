class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []


        for char in tokens:
            if char not in operators:
                stack.append(int(char)) 
            else:
                if char == '+':
                    result = stack[-2] + stack[-1] 
                elif char == '-':
                    result = stack[-2] - stack[-1] 
                elif char == '*':
                    result = stack[-2] * stack[-1] 
                elif char == '/' and stack[-1] != 0:
                    result = int(stack[-2] / stack[-1])
                else:
                    print("Wrong input")
                stack.pop()
                stack.pop()
                stack.append(result)

        return stack[0]

                