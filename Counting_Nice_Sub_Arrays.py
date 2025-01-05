class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMostK(nums, k):
            left = count = odd_count = 0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 != 0:
                        k += 1
                    left += 1
                count += (right - left + 1)
            return count
        
        return atMostK(nums, k) - atMostK(nums, k - 1)
        
