class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1=version1.split('.')
        s2=version2.split('.')
        ls1=len(s1)
        ls2=len(s2)
        if ls1>ls2:
            s2=s2+['0']*(ls1-ls2)
            l=ls1
        else:
            s1=s1+['0']*(ls2-ls1)
            l=ls2
        i=0
        while i<l:
            if int(s1[i])<int(s2[i]):
                return -1
            elif int(s1[i])>int(s2[i]):
                return 1
            else:
                i+=1
        return 0