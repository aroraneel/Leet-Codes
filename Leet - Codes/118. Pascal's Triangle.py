from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result


if __name__ == "__main__":
    sol = Solution()

    numRows = 5
    result = sol.generate(numRows)

    print("Pascal's Triangle with", numRows, "rows:")
    for row in result:
        print(row)

    # Summary:
    # This program generates Pascal's Triangle.
    # Each row starts and ends with 1.
    # Every middle element is the sum of the two elements
    # directly above it from the previous row.
    # The triangle is built row by row and stored in a list.