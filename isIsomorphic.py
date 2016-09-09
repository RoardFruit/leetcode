class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1={}
        d2={}
        n=len(s)
        for i in range(n):
            d1[s[i]]=d1.get(s[i],())+(i,)
            d2[t[i]]=d2.get(t[i],())+(i,)
        if set(d1.values())==set(d2.values()):
            return True
        return False