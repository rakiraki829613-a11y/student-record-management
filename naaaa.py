def prrfit(prices):
    minprice=prices[0]
    maxprice=0
    for prices in prices:
        minprice=min(minprice,prices)
        profit=minprice-prices
        maxprice=max(maxprice,prices)
        return maxprice
    prices=[1,2,3,4]
    print(prrfit(prices))