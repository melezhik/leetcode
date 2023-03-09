class Solution:
    def firstUniqChar(self, s: str) -> int:
      print(f"s: {s}")
      a = []
      for i in range(26):
        a.append(0)
      for c in s:
        o = ord(c) - 97
        a[o] += 1
      print(f"a: {a}")

      i = 0
      for c in s:
        o = ord(c) - 97
        if a[o] == 1:
          print(f"{c} is unique")
          return i 
        i+=1
      return -1

s = Solution()

r = s.firstUniqChar("leetcode")

print(f"r: {r}")


