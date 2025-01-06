class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_count = 0
        
        def is_strictly_increasing(arr):
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
        
        for i in range(n):
            for j in range(i, n):
                remaining = nums[:i] + nums[j+1:]
                if is_strictly_increasing(remaining):
                    total_count += 1
        
        return total_count
