# Runtime: 108 ms, faster than 79.18% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            row = set([])
            for element in r:
                if(element in row):
                    return False
                if(element != "."):
                    if(int(element) > 9):
                        return False
                    row.add(element)

        for x in range(len(board)):
            col = set([])
            for y in range(len(board)):
                temp = board[y][x]
                if(temp in col):
                    return False
                if(temp != "."):
                    if(int(temp) > 9):
                        return False
                    col.add(temp)

        for x in range(3):
            for y in range(3):
                box = set([])
                for r in range(3):
                    for c in range(3):
                        temp = board[(3)*x+r][(3)*y+c]
                        if(temp in box):
                            return False
                        if(temp != "."):
                            if(int(temp) > 9):
                                return False
                            box.add(temp)

        return True
