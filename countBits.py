class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l=[0]
        base=1
        for i in range(1,num+1):
            if i==2*base:
                base=i
            l.append(l[i-base]+1)
        return l
            