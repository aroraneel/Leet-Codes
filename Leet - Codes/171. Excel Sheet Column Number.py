from string import ascii_uppercase as asc

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {asc[i]: i + 1 for i in range(len(asc))}
        s = columnTitle[::-1]
        count = 0

        for i, j in enumerate(s):
            count += d[j] * (26 ** i)

        return count


if __name__ == "__main__":
    sol = Solution()

    columnTitle = "AB"
    result = sol.titleToNumber(columnTitle)

    print("Column Title:", columnTitle)
    print("Column Number:", result)

    # Summary:
    # This program converts an Excel column title into its corresponding number.
    # It creates a mapping of letters A-Z to numbers 1-26.
    # The string is reversed and processed like a base-26 number system.
    # Each character contributes its value multiplied by 26 raised to its position.