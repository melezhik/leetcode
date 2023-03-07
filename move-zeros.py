from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(f"nums: {nums}")
        l = 0
        for r in range(len(nums)):
          if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

        print(f"changed nums: {nums}")

s = Solution()
#s.moveZeroes([0])
#s.moveZeroes([0,1])
#s.moveZeroes([0,1,0])
#s.moveZeroes([0,1,0,0,0,0,1])
#s.moveZeroes([0,1,0,3,12])
#s.moveZeroes([2,1])
#s.moveZeroes([1,0,1])
