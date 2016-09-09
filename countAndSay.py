class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def Iter(ss):
            num=None
            string=''
            for s in ss:
                if num is None:
                    num=s
                    count=1
                elif s==num:
                    count=count+1
                else:
                    string=string+str(count)+num
                    count=1
                    num=s
            string=string+str(count)+num
            return string
        i=1
        s=str(1)
        while i<n:
            s=Iter(s)
            i=i+1
        return s
                            
            