class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=[1]
        l=[0,0,0]
        m=1
        for i in range(1,n):
            a,b,c=[p[l[0]]*2,p[l[1]]*3,p[l[2]]*5]
            m=min(a,b,c)
            p.append(m)
            if a==m:
                l[0]+=1
            if b==m:
                l[1]+=1
            if c==m:
                l[2]+=1
        return p[n-1]