from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
      print(f"height: {height}")
      l, r = 0, len(height) - 1
      max_l, max_r = 0, 0

      print(f"left: {l} | right: {r}")
      print(f"max_l: {l} | max_r: {r}")
      w = 0

      while l <= r:
        if max_l <= max_r:
          g = max_l - height[l]
          if g > 0:
            print(f"got some water from L {[l]} => + {g}")
            w = w + g
          else:
            print(f"no water at L {[l]}")
          if height[l] > max_l:
            max_l = height[l] # update max_l
            print(f"update max_l: {max_l}")
          l = l + 1 # shift to right 1 step
        else:
          g = max_r - height[r]
          if g > 0:
            print(f"got some water from R {[r]} => + {g}")
            w = w + g
          else:
            print(f"no water at R {[r]}")
          if height[r] > max_r:
            max_r = height[r] # update max_r
            print(f"update max_r: {max_r}")
          r = r - 1 # shift to left 1 step
      print(f"total water: {w}")
      return w

#height = [0,1,0,2,1,0,1,3,2,1,2,1]


s = Solution()

s.trap([4,2,0,3,2,5])

w = """
     #
#    #
#  # # 
## ###
## ###"""

print(w)
