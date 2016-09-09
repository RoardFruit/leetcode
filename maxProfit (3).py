class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=1:
            return 0
        profit=[-prices[0],0,0]
        for i in range(1,n):
            p0=profit[0]
            p1=profit[1]
            p2=profit[2]
            profit[0]=max(p0,p2-prices[i])
            profit[1]=p0+prices[i]
            profit[2]=max(p2,p1)
        return max(profit)