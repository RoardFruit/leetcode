#º¯ÊýÊ½µÝ¹é
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la=len(a)
        lb=len(b)
        if la<lb:
            a=a.zfill(lb)
            l=lb
        else:
            b=b.zfill(la)
            l=la
        def Iter(i,flag):
            if i<0:
                return str(flag)
            else:
                return Iter(i-1,(int(a[i])+int(b[i])+flag)/2)+str((int(a[i])+int(b[i])+flag)%2)
        result=Iter(l-1,0)
        if result[0]=='0':
           return result[1:]
        return result
       
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la=len(a)
        lb=len(b)
        i=la-1
        j=lb-1
        result=[]
        flag=0
        while i>=0 or j>=0:
            if i>=0:
                aa=a[i]
            else:
                aa='0'
            if j>=0:
                bb=b[j]
            else:
                bb='0'
            if aa=='0' and bb=='0' and flag==0:
                flag=0
                result.append('0')
            elif aa=='1' and bb=='1' and flag==0:
                flag=1
                result.append('0')
            elif (aa=='1' or bb=='1') and flag==0:
                flag=0
                result.append('1')
            elif aa=='0' and bb=='0' and flag==1:
                flag=0
                result.append('1')
            elif aa=='1' and bb=='1' and flag==1:
                flag=1
                result.append('1')
            elif (aa=='1' or bb=='1') and flag==1:
                flag=1
                result.append('0')
            i=i-1
            j=j-1
        if flag==1:
            result.append('1')
        result.reverse()
        return ''.join(result)
                