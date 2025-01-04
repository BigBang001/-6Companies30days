import random

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.areas = []
        area = 0
        for x1, y1, x2, y2 in rects:
            area += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.areas.append(area)
        

    def pick(self):
        """
        :rtype: List[int]
        """
        rnd = random.randint(1, self.areas[-1])
        idx = bisect.bisect_left(self.areas, rnd)
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
