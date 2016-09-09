class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=list(bin(n).replace('0b',''))
        s=['0']*(32-len(s))+s          
        s.reverse()                    
        return int(''.join(s),2)       