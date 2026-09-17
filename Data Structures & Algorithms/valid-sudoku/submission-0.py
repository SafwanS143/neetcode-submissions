class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        columns = []
        boxes = []

        for j in range(9):
            rows.append(set())
        for j in range(9):
            columns.append(set())
        for j in range(9):
            boxes.append(set())

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                boxNum = (r // 3) * 3 + (c // 3) 

                if num != "." and (num in rows[r] or num in columns[c] or num in boxes[boxNum]):

                    return False

                rows[r].add(num)
                columns[c].add(num)
                boxes[boxNum].add(num)


        return True