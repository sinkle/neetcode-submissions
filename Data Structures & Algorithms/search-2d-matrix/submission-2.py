class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        d, t = 0, len(matrix) - 1

        while d < t:
            i = (t - d) // 2 + d
            if target < matrix[i][0]:
                t = i - 1
            elif target > matrix[i][-1]:
                d = i + 1
            else:
                d = i
                break
        
                
        i = d
        l, r = 0, len(matrix[i]) - 1
        if matrix[i][l] == target:
            return True
        if matrix[i][r] == target:
            return True

        while l < r:
            m = (r - l) // 2 + l
            if target < matrix[i][m]:
                r = m - 1
            elif target > matrix[i][m]:
                l = m + 1
            else:
                return True

        return False