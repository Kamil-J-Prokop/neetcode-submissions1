class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        left = 0
        candidate_row = -1

        if matrix[top][left] > target or not matrix:
            return False

        bottom = len(matrix)
        right = len(matrix[0])

        #print(f"Start: Top: {top}, bottom: {bottom}, left: {left}, right: {right}")

        while top < bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid
            else:
                candidate_row = mid
                top = mid + 1
            #print(f"Loop: Top: {top}, bottom: {bottom}, left: {left}, right: {right}, mid: {mid}, candidate: {candidate_row}")
        
        #print(f"Candidate row: {candidate_row}")

        while left < right:
            mid = left + (right - left) // 2
            #print(mid)
            if matrix[candidate_row][mid] == target:
                return True
            elif matrix[candidate_row][mid] < target:
                left = mid + 1
            else:
                right = mid

        return False



        