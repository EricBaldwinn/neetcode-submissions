class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue
                
                if ((r, num)) in rows:
                    return False
                rows.add((r, num))

                if ((num, c)) in cols:
                    return False
                cols.add((num, c))

                box_row = r // 3
                box_col = c // 3

                if ((box_row, box_col, num)) in boxes:
                    return False
                boxes.add((box_row, box_col, num))
        return True
        