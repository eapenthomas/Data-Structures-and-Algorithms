def btime_to_buyE_sell(prices):
   small = float('inf')
   maxprofit = 0
   for p in prices:
       if p<small:
           small = p
       else:
           maxprofit = max(maxprofit,p-small)
   return maxprofit

print(btime_to_buyE_sell([9,2,8,4,6,12]))