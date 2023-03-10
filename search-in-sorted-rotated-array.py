from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      print(f"nums: {nums} | target: {target}")

      l, r = 0, len(nums) - 1

      m = (l + r) // 2

      print(f"l: {l} | r: {r} | m: {m}")

      while l <= r:
        if nums[m] == target:
          print(f"found target {target} at index [{m}]")
          return m
        # we in left sorted array
        if nums[m] >= nums[l]:
          if target > nums[m]:
            # search in right
            l = m + 1
          elif target < nums[m] and target < nums[l]:
            # search in right
            l = m + 1
          else:
            # search in left
            r = m - 1
        # we are in right sorted array
        else:
          if target < nums[m]:
            # search in left
            r = m - 1
          elif target > nums[m] and target > nums[r]:
            # search in left
            r = m - 1
          else:
            # search in right
            l = m + 1
        m = (l + r) // 2
        print(f"m: {m} => {nums[m]}")
      print("target not found")
      return -1

s = Solution()

s.search([4,5,6,7,0,1,2],0)

s.search([0,1,0],11)
