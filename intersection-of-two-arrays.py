from typing import List;

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      print(f"nums1: {nums1}")
      print(f"nums2: {nums2}")
      nums1.sort()
      nums2.sort()
      print(f"nums1 sort: {nums1}")
      print(f"nums2 sort: {nums2}")

      i, j = 0,0

      ret = []

      while i < len(nums1) and j < len(nums2):
        print(f"i={i} => {nums1[i]} | j={j} => {nums2[j]}")
        if nums1[i] == nums2[j]:
          print("\tfound duplicates")
          ret.append(nums1[i])
          i = i + 1
          j = j + 1
        elif nums1[i] > nums2[j]:
          j = j + 1
        else:
          i = i + 1
      print(f"intersect: {ret}")
      return ret
s = Solution()

s.intersect([1,2,2,1],[2,2])

