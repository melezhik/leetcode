from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(f"s: {s}")
        l,r = 0, len(s) - 1
        while l < r:
          s[l], s[r] = s[r], s[l]
          l += 1
          r -= 1
        print(f"reverse: {s}")
s = Solution()

s.reverseString(["H","a","n","n","a","h"])
s.reverseString(["H"])
s.reverseString(["H","H"])
s.reverseString(["H","h"])
s.reverseString(["H","h", "H"])
s.reverseString([])

