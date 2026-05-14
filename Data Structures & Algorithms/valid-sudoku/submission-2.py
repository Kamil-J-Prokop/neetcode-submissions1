class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            present_numbers = set()
            for element in row:
                if element in present_numbers and element != ".":
                    return False
                else:
                    present_numbers.add(element)

        i = 0
        j = 0
        
        while j < len(board):
            present_numbers = set()

            while i < len(board[0]):
                if board[i][j] in present_numbers and board[i][j] != ".":
                    return False
                else:
                    present_numbers.add(board[i][j])
                #print("Iteration step:")
                #print(board[i][j])
                i += 1    
            j += 1
            i = 0
        
        stride = 3
        i = 1
        j = 1
        while i <= 7 and j <= 7:
            row = -1
            col = -1
            present_numbers = set()
            while row <= 1:
                while col <= 1:
                    element = board[i + row][j + col]
                    #print("Iteration:")
                    #print(element)
                    if element in present_numbers and element != ".":
                        return False
                    else:
                        present_numbers.add(element)
                    col += 1
                row += 1
                col = -1
            if i != 7:
                i += stride
            else:
                i = 1
                j += stride
        return True        

"""
#GPT one pass:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                element = board[row][col]

                if element == ".":
                    continue

                box_index = (row // 3) * 3 + (col // 3)

                if (
                    element in rows[row]
                    or element in cols[col]
                    or element in boxes[box_index]
                ):
                    return False

                rows[row].add(element)
                cols[col].add(element)
                boxes[box_index].add(element)

        return True
"""

"""
#readable gpt

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()

            for col in range(9):
                element = board[row][col]

                if element == ".":
                    continue

                if element in seen:
                    return False

                seen.add(element)

        for col in range(9):
            seen = set()

            for row in range(9):
                element = board[row][col]

                if element == ".":
                    continue

                if element in seen:
                    return False

                seen.add(element)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        element = board[row][col]

                        if element == ".":
                            continue

                        if element in seen:
                            return False

                        seen.add(element)

        return True
"""