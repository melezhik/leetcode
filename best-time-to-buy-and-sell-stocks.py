from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      print(prices)
      print("OK")
      have_stock = False
      hp = 0 # hold price - price of stock we have
      profit = 0

      for i in range(len(prices)-1):
        print(f"parse {i} => {prices[i]}")
        cp = prices[i]
        np = prices[i+1]
        print(f"cp: {cp} | np: {np}")
        if have_stock == True:
          # we have some stock
          # so we can choose
          # to sell them
          if cp > np:
            # sell stock if next price
            # is less then our current price (hp)
            print(f"sell profit: {cp - hp}")
            profit += (cp - hp)
            have_stock = False
        else:
          # we don't have any stocks,
          # so we can choose to buy something
          if cp > np:
            # next day price is less then
            # current price
            # don't buy
            pass
          else:
            # buy!
            hp = cp
            print(f"buy at: {hp}")
            have_stock = True
      if have_stock == True:
        print(f"edge case, hp: {hp}, np: {np}")
        # edge case
        # if we've bought something
        # but did did not sell it
        profit += (np - hp)

      print(f"total profit: {profit}")
      return profit
s = Solution()

# s.maxProfit([7,1,5,3,6,4])
s.maxProfit([2,1,2,0,1])
