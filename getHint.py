class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n=len(secret)
        bulls=0
        cows=0
        s=[]
        g=[]
        for i in range(n):
                if secret[i]==guess[i]:
                    bulls=bulls+1
                else:
                    s.append(secret[i])
                    g.append(guess[i])
        for char in g:
            if char in s:
                cows=cows+1
                s.remove(char)
        return str(bulls)+'A'+str(cows)+'B'
        