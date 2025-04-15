## 1. Longest Common Subsequence (Tabular Method)
def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Finds the longest common subsequence of two strings using dynamic programming.
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    # print(dp)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print("DP Table:",i)
        for row in dp:
            print(" ".join(f"{cell}" for cell in row))

    print("DP Table:")
    for row in dp:
        print(" ".join(f"{cell}" for cell in row))

    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs

def test_longest_common_subsequence():
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    return result

print(test_longest_common_subsequence())
