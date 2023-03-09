class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      print(f"cmp: {s} and {t}")
      s1 = {}
      for i in s:
        print(f"a={i}")
        if i in s1:
          s1[i] += 1
        else:
          s1[i] = 1
      print("======")
      for i in t:
        print(f"t={i}")
        if i in s1:
          s1[i] -= 1
        else:
          return False

      for v in s1.values():
        if v != 0:
          return False

      return True

s = Solution()

ss = "anagram"
tt = "nagaram"

a=s.isAnagram(ss,tt)

print(f"a={a}")
