from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      print(f"n: {n}")
      res = []
      s = []

      def hop (oc: int, cc: int):

        print(f"enter hop: oc={oc} | cc={cc}")

        if oc == cc == n:
          st = "".join(s)
          print(f"hit the limit: {s} => {st}")
          res.append(st)
          return

        if oc > cc:
          s.append(")")
          hop(oc,cc+1)
          s.pop()

        if oc < n:
          s.append("(")
          hop(oc+1,cc)
          s.pop()

      hop(0,0)
      print(f"res: {res}")
      return res

s = Solution()

s.generateParenthesis(3)
