
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(f"matrix: {matrix}")
        l, r = 0, len(matrix) - 1
        print(f"l={l} | r={r}")
        #top, bottom = l, r
        while l < r:
          #top, bottom = l, r
          for i in range(r-l):
            temp = matrix[l][l+i]
            matrix[l][l+i] = matrix[r-i][l]
            matrix[r-i][l] = matrix[r][r-i]
            matrix[r][r-i] = matrix[l+i][r]
            matrix[l+i][r] = temp

          l += 1
          r -= 1
        print(f"rotated matrix: {matrix}")

s = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

s.rotate(matrix)


"""

1, 2, 3
4, 5, 6
7, 8, 9


7, 4, 1
8, 5, 2
9, 6, 3

"""
