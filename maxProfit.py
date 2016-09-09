class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        min=None
        profit=0
        for i in prices:
            if not min is None and i>min:
                if i-min>profit:
                    profit=i-min
            else:
                min=i
        return profit