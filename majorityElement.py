class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x={}
        for num in nums:
            x[num]=x.get(num,0)+1
        large=None
        largenum=None
        for k,v in x.items():
            if large is None or v>large:
                large=v
                largenum=k
        return largenum
        
            