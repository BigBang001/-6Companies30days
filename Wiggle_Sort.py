class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n - 1) // 2
        left = nums[:mid + 1][::-1]
        right = nums[mid + 1:][::-1]

        for i in range(n):
            if i % 2 == 0:
                nums[i] = left.pop(0)
            else:
                nums[i] = right.pop(0)
