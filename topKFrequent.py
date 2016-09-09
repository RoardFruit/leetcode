class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numCur={}
        for num in nums:
            numCur[num]=numCur.get(num,0)+1
        sortvk=sorted([(v,key) for key,v in numCur.items()],reverse=True)
        result=[]
        for v,key in sortvk[:k]:
            result.append(key)
        return result
        