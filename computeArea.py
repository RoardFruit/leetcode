class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total=(C-A)*(D-B)+(G-E)*(H-F)
        area=max((min(G,C)-max(A,E)),0)*max((min(D,H)-max(F,B)),0)
        return total-area

        