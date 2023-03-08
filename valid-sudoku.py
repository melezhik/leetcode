from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      cols = collections.defaultdict(set)
      rows = collections.defaultdict(set)
      sq = collections.defaultdict(set)

      for r in range(9):
        for c in range(9):
          d = board[c][r]
          if d == ".":
            continue
          elif d in cols[c] or d in rows[r] or d in sq[(r//3,c//3)]:
            return False
          else:
            cols[c].add(d); rows[r].add(d); sq[(r//3,c//3)].add(d)
      return True
s = Solution()

board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board))
