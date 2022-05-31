class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)/2
        n_types = len(set(candyType))
        return min([n, n_types])