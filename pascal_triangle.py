from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def buildTriangleRows(rows: List[List[int]], numRows: int) -> List[List[int]]:
            if numRows == 0:
                return rows
            return buildTriangleRows(
                rows + [buildTriangleColumns([], 0, rows[-1])], numRows - 1
            )

        def buildTriangleColumns(
            columns: List[int], index: int, lastRow: List[int]
        ) -> List[int]:
            if index == (len(lastRow) + 1):
                return columns
            return buildTriangleColumns(
                columns + [buildTriangleColumn(index, lastRow)], index + 1, lastRow
            )

        def buildTriangleColumn(index: int, lastRow: List[int]):
            if index == 0 or index == len(lastRow):
                return 1
            return lastRow[index - 1] + lastRow[index]

        if numRows > 1:
            return buildTriangleRows([[1]], numRows - 1)

sol = Solution()
print(sol.generate(10))
