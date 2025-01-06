class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindrome(mask, s):
            subseq = [s[i] for i in range(len(s)) if mask & (1 << i)]
            return subseq == subseq[::-1]

        n = len(s)
        dp = {}

        for mask in range(1, 1 << n):
            if is_palindrome(mask, s):
                dp[mask] = bin(mask).count('1')

        max_product = 0
        
        for mask1 in dp:
            for mask2 in dp:
                if mask1 & mask2 == 0:
                    max_product = max(max_product, dp[mask1] * dp[mask2])
        
        return max_product
