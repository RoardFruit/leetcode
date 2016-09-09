class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set()
        next=n
        while True:
            if next in s:
                return False
            else:
                if next==1:
                    return True
                s.add(next)
                next=sum(map(lambda x:x*x,[int(i) for i in str(next)])) 