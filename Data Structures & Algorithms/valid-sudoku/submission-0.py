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