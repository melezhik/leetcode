from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      print(f"digits: {digits}")
      i = len(digits) - 1
      while i >= 0:
        print(f"parse i={i} => {digits[i]}")
        if digits[i] != 9:
          digits[i] = digits[i] + 1
          print(f"\tnormal incriment: {digits[i]}")
          break
        else:
          while digits[i] == 9:
            digits[i] = 0
            if i == 0:
              break
            else:
              i = i - 1
          if digits[i] == 0:
            print(f"handleA, i={i} => {digits[i]}")
            digits.insert(0,1)
          else:
            print("handleB")
            digits[i] = digits[i]+1
          break
        i = i - 1
      print(f"changed digits: {digits}")
s = Solution()

#s.plusOne([1,2,3])
#s.plusOne([1,0,9,9,9])
s.plusOne([9,9,9,9])
#s.plusOne([8,9,9,9])
