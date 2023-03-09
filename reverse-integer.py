import math
class Solution:
    def reverse(self, x: int) -> int:
      print(f"x: {x}")
      max_32 = pow(2,31) - 1
      min_32 = - pow(2,31)
      print(f"max_32: {max_32} | min_32: {min_32}")
      res = 0
      while x:
        print("VVVV")
        d = int(math.fmod(x,10))
        x = int(x / 10)
        print(f"x: {x} | d: {d}")
        #break
        if res == 214748364 and d > 7:
          print("AA")
          return 0
        elif res > 214748364:
          print("BB")
          return 0
        elif res == -214748364 and d < -8:
          print("CC")
          return 0
        elif res < -214748364:
          print("DD")
          return 0
        else:
          print("EE")
          print(f"res: {res}")
          res = res * 10 + d
      print(f"res: {res}")
      return res

s = Solution()

s.reverse(123)
#s.reverse(-123)
#s.reverse(123456780)


