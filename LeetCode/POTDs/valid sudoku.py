class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        square=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue
                if num in row[i] or num in col[j] or num in square[(i//3,j//3)]:
                    return False
                row[i].add(num)
                col[j].add(num)
                square[(i//3,j//3)].add(num)
        return True
