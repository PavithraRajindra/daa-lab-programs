## 2. Matrix Chain Multiplication (Tabular Method)
import math

def matrix_chain_multiplication(dimensions: list[int]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """
    n = len(dimensions) - 1
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    split = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = math.inf
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    splits = []
    def get_splits(i, j):
        if i < j:
            k = split[i][j]
            splits.append((i, j, k))
            get_splits(i, k)
            get_splits(k + 1, j)

    get_splits(1, n)
    return dp[1][n], splits

def test_matrix_chain_multiplication():
    dims = [40, 20, 30, 10, 30]
    cost, splits = matrix_chain_multiplication(dims)
    return cost, splits

print(test_matrix_chain_multiplication())

