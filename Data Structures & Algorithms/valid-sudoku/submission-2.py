class Solution:
    def is_valid(self, values: List[str]) -> bool:
            seen = set()
            for val in values:
                if val != '.':
                    if val in seen:
                        return False
                    else:
                        seen.add(val)
            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nine = 9
        if not board or len(board) != nine or len(board[0]) != nine:
            return False

        for group in range(nine):
            if not self.is_valid(board[group]): return False
            if not self.is_valid([row[group] for row in board]): return False
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(board[(group//3)*3+i][(group%3)*3+j])
            if not self.is_valid(box): return False
        return True


