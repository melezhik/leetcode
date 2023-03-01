from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      print(nums)
      p = 0 # pointer to the last unique element
            # in nums array
            # unique elements are placed in the head
            # of the initial array
      for i in range(len(nums)):
        print(f"handle: {i} => {nums[i]}")
        if i == 0:
          pass # nothing to do with the very first element
        else:
          if nums[i] != nums[p]:
            # we have another unique element
            # let's shift p and increase c
            # and put the element
            # to the head
            print(f"uniq: {nums[i]}")
            p = p + 1
            nums[p] = nums[i] # change in place
            print(f"p increased: {p}, nums[p]: {nums[p]}")
      print(p+1)
      return p+1

s = Solution()

s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
