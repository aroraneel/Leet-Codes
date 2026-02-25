from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        for i in range(rowIndex + 1):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result[rowIndex]


if __name__ == "__main__":
    sol = Solution()

    rowIndex = 4
    result = sol.getRow(rowIndex)

    print("Row Index:", rowIndex)
    print("Pascal Row:", result)

    # Summary:
    # This program returns a specific row of Pascal’s Triangle.
    # It builds the triangle row by row up to the given index.
    # Each row starts and ends with 1.
    # Middle elements are calculated using the previous row.
    # Finally, it returns the row at the given index.