import numpy as np

def simplex(tableau: np.ndarray):
    num_rows, num_cols = tableau.shape

    while True:
        z_row = tableau[0, 1:-1]
        pivot_col_index = np.argmax(z_row)+1

        if tableau[0, pivot_col_index] <=0:
            break

        ratios = []

        for i in range(1, num_rows):
            col_val = tableau[i, pivot_col_index]
            rhs_val = tableau[i, -1]
            if col_val > 0:
                ratios.append(rhs_val/col_val)
            else:
                ratios.append(np.inf)

        pivot_row_index = np.argmin(ratios) + 1

        pivot_element = tableau[pivot_row_index, pivot_col_index]

        tableau[pivot_row_index] /= pivot_element

        for i in range(num_rows):
            if i != pivot_row_index:
                row_factor = tableau[i, pivot_col_index]
                tableau[i] -= row_factor * tableau[pivot_row_index]
        
    solution = {f"x{i+1}": 0.0 for i in range(2)}
    # for i in range(num_rows - 1):
    #     for j in range(num_cols - 1):
    #         if tableau[i][j] == 1 and all(tableau[k][j] == 0 for k in range(num_rows) if k != i):
    #             solution[f"x{j+1}"] = tableau[i, -1]
    #             break
    for j in range(2):
        col = tableau[:, j + 1]  # Skip Z column at index 0
        if list(col[1:]).count(0) == len(col) - 2 and list(col[1:]).count(1) == 1:
            row_index = list(col[1:]).index(1) + 1
            solution[f"x{j+1}"] = tableau[row_index, -1]
    return tableau[0, -1], solution
    
def test_simplex_method():
    tableau = np.array([
        [1, 4, 7, 0, 0, 0],
        [0, 4, 3, 1, 0, 12],
        [0, 2, 4, 0, 1, 12]
    ], dtype=float)
    # max_value, sol = simplex(tableau)
    ans = simplex(tableau)
    return ans
    # return max_value, sol

print(test_simplex_method())