from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      h = heights
      print(f"h: {h}")
      s = []
      i = 0
      max = 0
      while i < len(h):
        if not s:
          print(f"(init) add index: {i} to stack")
          s.append(i)
          i = i + 1
        elif h[i] >= h[s[-1]]:
          print(f"add index: {i} to stack")
          s.append(i)
          i = i + 1
        else:
          top = s.pop()
          if len(s):
            a = h[top]*(i - s[-1] -1)
          else:
            a = h[top]*i

          if a > max:
            max = a
      print(f"stack reminder: {s} | max: {max}")
      while len(s) > 0:
          t = s.pop()
          if len(s):
            a = h[t]*(i - s[-1] -1)
          else:
            a = h[t]*i
          if a > max:
            max = a

      print(f"max: {max}")

      return max

s = Solution()

#s.largestRectangleArea([])
s.largestRectangleArea([2])
s.largestRectangleArea([2,2])

s.largestRectangleArea([2,1,5,6,2,3])


print("""
   @
  @@
  @@
  @@ @
@ @@@@
@@@@@@
012345
""")
