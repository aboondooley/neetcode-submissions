class Solution:
    def is_valid(self, values) -> bool:
        exists = set()
        for val in values:
            if val != '.':
                if val in exists:
                    return False
                else:
                    exists.add(val)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check dupes
        # calculate box coordinates
        nine = 9
        # check rows:
        if not board or len(board) != nine or len(board[0]) != nine: return False
        for i in range(nine):
            if not self.is_valid(board[i]): return False
        for i in range(nine):
            if not self.is_valid([r[i] for r in board]): return False
        if not self.is_valid(board[0][:3]+board[1][:3]+board[2][:3]): return False
        if not self.is_valid(board[0][3:6]+board[1][3:6]+board[2][3:6]): return False
        if not self.is_valid(board[0][6:]+board[1][6:]+board[2][6:]): return False
        if not self.is_valid(board[3][0:3]+board[4][0:3]+board[5][0:3]): return False
        if not self.is_valid(board[3][3:6]+board[4][3:6]+board[5][3:6]): return False
        if not self.is_valid(board[3][6:]+board[4][6:]+board[5][6:]): return False
        if not self.is_valid(board[6][:3]+board[7][:3]+board[8][:3]): return False
        if not self.is_valid(board[6][3:6]+board[7][3:6]+board[8][3:6]): return False
        if not self.is_valid(board[6][6:]+board[7][6:]+board[8][6:]): return False   

        return True

