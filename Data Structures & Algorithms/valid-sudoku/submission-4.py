class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            r = []
            c = []
            m = []
            for j in range(0, 9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in r:
                    return False
                else:
                    r.append(board[i][j])

                if board[j][i] == '.':
                    pass
                elif board[j][i] in c:
                    return False
                else:
                    c.append(board[j][i])

                m_j = j % 3 + (i % 3) * 3
                m_i = j // 3 + (i // 3) * 3
                if board[m_i][m_j] == '.':
                    pass
                elif board[m_i][m_j] in m:
                    return False
                else:
                    m.append(board[m_i][m_j])

        return True

                