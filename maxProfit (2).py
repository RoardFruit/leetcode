class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        min=None
        for price in prices:
            if min is None or price<min:
                min=price
            elif price>min:
                profit+=price-min
                min=price
        return profit
            