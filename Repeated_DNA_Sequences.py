class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen, repeated = set(), set()
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                repeated.add(sub)
            seen.add(sub)
        return list(repeated)
