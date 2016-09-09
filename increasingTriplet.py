class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=[]
        for num in nums:
            n=len(l)
            if n==0:
                l.append(num)
            elif n==1:
                if num>l[0]:
                    l.append(num)
                else:
                    l[0]=num
            else:
                if num>l[1]:
                    return True
                elif num>l[0]:
                    l[1]=num
                else:
                    l[0]=num
        return False
                
                