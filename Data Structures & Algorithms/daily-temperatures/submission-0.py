class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            current_temp = temperatures[i]
            
            while stack and current_temp >= stack[-1][0]:
                stack.pop()
            
            if stack:
                output[i] = stack[-1][1] - i



            stack.append((current_temp, i))

        return output
            

