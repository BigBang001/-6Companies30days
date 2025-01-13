def matrixChainOrder(arr):
    n = len(arr) - 1
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i] * arr[k + 1] * arr[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    
    def constructOrder(i, j):
        if i == j:
            return chr(ord('A') + i)
        k = split[i][j]
        left = constructOrder(i, k)
        right = constructOrder(k + 1, j)
        return f"({left}{right})"
    
    return constructOrder(0, n - 1)
