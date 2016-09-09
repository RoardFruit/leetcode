class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            if d.get(nums[i],None) is None:
                d[nums[i]]=i
            elif i-d[nums[i]]<=k:
                return True
            else:
                d[nums[i]]=i
        return False