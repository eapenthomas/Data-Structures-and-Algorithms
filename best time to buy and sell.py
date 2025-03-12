def btime_to_buyE_sell(prices):
    small = float('inf')
    maxprofit = 0
    for price in prices:
        if price < small:
            small = price
        else:
            maxprofit = max(maxprofit, price - small)
    return maxprofit

print(btime_to_buyE_sell([2,5,3,4,9]))