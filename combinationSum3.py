class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        start=range(1,10)
        def combinationSumIter(l,k,n,r):
            if k==n==0:
                res.append(r)
            elif k<0 or n<0:
                pass
            elif len(l)==1:
                if k==1 and n==l[0]:
                    res.append(r+[l[0]])
            else:
                combinationSumIter(l[1:],k-1,n-l[0],r+[l[0]])
                combinationSumIter(l[1:],k,n,r)
        combinationSumIter(start,k,n,[])
        return res