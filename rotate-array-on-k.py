from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      print(nums)
      k = k % len(nums)
      print(f"k:{k}")
      # reverse array first
      l, r = 0, len(nums) - 1
      while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
      print(f"reverse nums: {nums}")

      l, r = 0, k - 1
      while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
      print(f"nums part 1: {nums}")

      l, r = k, len(nums) - 1
      while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
      print(f"nums part 2: {nums}")

c = Solution()

c.rotate([1,2,3,4,5,6,7],3)

