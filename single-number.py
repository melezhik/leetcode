from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      cxor = nums[0]
      print(nums)
      for i in range(1,len(nums)):
        cxor = cxor ^ nums[i]
        print(f"cxor: {cxor}")
      print(f"uniq: {cxor}")

c = Solution()

c.singleNumber([1,2,3,2,1])

c.singleNumber([4,1,2,1,2])
