class Solution(object):
    def maxProfit(self, prices):
        j=1
        i=0
        max=0
        while j<len(prices):
              if prices[j]>prices[i]:
                   n=prices[j]-prices[i]   
                   if n>max:
                       max=n
                   
              else:
                   i=j
              j+=1     
        return max                     