class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
        result = []

        while columnNumber > 0:
            result.append(capitals[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26

        result.reverse()
        return ''.join(result)


if __name__ == "__main__":
    sol = Solution()

    columnNumber = 28
    result = sol.convertToTitle(columnNumber)

    print("Column Number:", columnNumber)
    print("Excel Column Title:", result)

    # Summary:
    # This program converts a column number into its corresponding Excel column title.
    # It repeatedly calculates the remainder when divided by 26.
    # Each remainder maps to a letter from A to Z.
    # The result is reversed at the end to form the correct title.