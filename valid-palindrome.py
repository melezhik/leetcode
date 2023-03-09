class Solution:
    def isPalindrome(self, s: str) -> bool:
      l = 0
      r = len(s)-1
      print(f"s: {s}")
      print(f"start l:{l} r:{r}")
      while l < r:
        print(f"handle: l: [{s[l]}] | r: [{s[r]}]")
        if not s[l].isalnum():
          print(f"l: skip [{s[l]}]")
          l+=1
          continue
        if not s[r].isalnum():
          print(f"r: skip [{s[r]}]")
          r-=1
          continue
        print(f"cmp: l={s[l]} and r={s[r]}")
        if s[l].lower() != s[r].lower():
          return False
        l += 1
        r -= 1
        print(f"next: l={l} r={r}")
      return True

s = Solution()

r = s.isPalindrome("A man, a plan, a canal: Panama")

print(f"r: {r}")
