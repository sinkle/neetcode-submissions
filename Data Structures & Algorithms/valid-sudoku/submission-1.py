class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in board:
            row_set = []
            for row_el in r:
                if row_el not in row_set:
                    if row_el != '.':
                        row_set.append(row_el)
                else:
                    return False

        # check columns
        for n in range(9):
            col_set = []
            for col in board:
                col_el = col[n]
                if col_el not in col_set:
                    if col_el != '.':
                        col_set.append(col_el)
                else:
                    return False

        # check squares
        for c_n in range(0, 3):
            for r_n in range(0, 3):
                helper = []
                for s_c_n in range(c_n * 3, c_n * 3 + 3):
                    for s_r_n in range(r_n * 3, r_n * 3 + 3):
                        el = board[s_r_n][s_c_n]
                        if board[s_r_n][s_c_n] not in helper:
                            if el != '.':
                                helper.append(el)
                        else:
                            return False

        return True