from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      print(f"nums: {nums}")
      hash = set()
      for i in nums:
        if i in hash:
          return True
        hash.add(i)
      return False

s = Solution()

s.containsDuplicate([1,2,3,1])
