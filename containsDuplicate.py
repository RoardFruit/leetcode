class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x={}
        for num in nums:
            x[num]=x.get(num,0)+1
            if x[num]>1:
                return True
        return False