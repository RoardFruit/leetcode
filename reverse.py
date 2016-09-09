class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=list(str(x))
        if s[0]=='-':
            s=s[1:]
            s.append('-')
        s.reverse()
        result=int(''.join(s))
        if result>2147483647 or result<-2147483647:
            return 0
        return result