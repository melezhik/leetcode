from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hash = {}
      print(f"nums: {nums} | target: {target}")
      for i,n in enumerate(nums):
        diff = target - n
        if diff in hash:
          print(f"return: {i}, {hash[diff]}")
          return [ i, hash[diff]]
        else:
          hash[n] = i

s = Solution()

s.twoSum([2,7,11,15],9)
