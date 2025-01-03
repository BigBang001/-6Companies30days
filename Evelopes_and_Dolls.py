class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    
        lis = []
        for _, h in envelopes:
          pos = bisect_left(lis, h)
          if pos == len(lis):
            lis.append(h)
          else:
            lis[pos] = h
    
        return len(lis)
        
