class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2

            # target > largest value in the row

            if target > matrix[row][-1]:
                top = row + 1

            # target < smallest value in the row

            elif target < matrix[row][0]:
                bottom = row - 1

            # target in this row - binary search in this row
            else: break

        if not (top <= bottom): return False # no rows contain target value

        row = (top + bottom) // 2

        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1

            elif target < matrix[row][m]:
                r = m - 1

            else:
                return True
        return False