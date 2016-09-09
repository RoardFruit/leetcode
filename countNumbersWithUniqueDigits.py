class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=10
        if n==0:
            return 1
        elif n==1:
            return 10
        sum=9
        for i in range(2,n+1):
            sum*=9-i+2
            total+=sum
        return total