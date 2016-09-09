class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combineIter(start,to,k):
            if to-start+1<k:
                return []
            if k==1:
                return [[i] for i in range(start,to+1)]
            return [[head]+tail for head in range(start,to-k+2) for tail in combineIter(head+1,to,k-1)]
        return combineIter(1,n,k)
        