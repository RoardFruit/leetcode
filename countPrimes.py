class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        primes=[2]
        i=3
        numsPrime=1
        while i<n:
            j=0
            while j<numsPrime:
                if i%primes[j]==0:
                    break
                j=j+1
            if j==numsPrime:
                primes.append(i)
                numsPrime=numsPrime+1
            i=i+1
        return numsPrime
                