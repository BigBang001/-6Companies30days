class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        result = []
        dq = deque()
    
        for i in range(len(arr)):
          if dq and dq[0] == i - k:
            dq.popleft()
          while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
          dq.append(i)
          if i >= k - 1:
            result.append(arr[dq[0]])
    
        return result
