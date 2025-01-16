class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
       
        char_count = Counter(s)
        
        for idx, char in enumerate(s):
            if char_count[char] == 1:
                return idx

        return -1
