class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k=len(primes)
        p=[1]
        l=[0]*k
        for i in range(1,n):
            minList=[p[l[index]]*primes[index] for index in range(k)]
            m=min(minList)
            p.append(m)
            for index in range(k):
                if m==minList[index]:
                    l[index]+=1
        return p[-1]