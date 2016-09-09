class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n=len(citations)
        if n==0:
            return 0
        def Iter(start,to):
            if start>=to:
                if n-start<=citations[start]:
                    return n-start
                else:
                    return n-start-1
            mid=(start+to)/2
            if n-mid<citations[mid]:
                return Iter(start,mid-1)
            elif n-mid>citations[mid]:
                return Iter(mid+1,to)
            else:
                return n-mid
        return Iter(0,n-1)