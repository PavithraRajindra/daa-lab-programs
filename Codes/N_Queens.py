## 6. N-Queens Problem (Backtracking)
def solve_nqueens(n: int) -> list[list[int]]:
    """
    Time Complexity: O(N!)
    Space Complexity: O(N^2) or O(N) with optimized constraints
    """
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            print(board)
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)
    return solutions

def test_solve_nqueens():
    solutions = solve_nqueens(4)
    return solutions

ans = test_solve_nqueens()
for row in ans:
    print(row)