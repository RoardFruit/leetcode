class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n=len(citations)
        for i in range(n):
            if n-i<=citations[i]:
                return n-i
        return 0
            