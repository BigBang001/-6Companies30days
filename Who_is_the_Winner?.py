class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def josephus(n, k):
         if n == 1:
            return 0
         return (josephus(n - 1, k) + k) % n

        return josephus(n, k) + 1
