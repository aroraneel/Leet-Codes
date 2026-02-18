from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curstr + c)

        if digits:
            backtrack(0, "")

        return res


if __name__ == "__main__":
    sol = Solution()

    digits = "23"
    result = sol.letterCombinations(digits)

    print("Digits:", digits)
    print("Letter Combinations:", result)

    # Summary:
    # This program generates all possible letter combinations for a phone number string.
    # Each digit maps to a set of characters like on a telephone keypad.
    # It uses backtracking to build combinations by choosing one letter at a time.
    # When the length matches the digits length, the combination is added to the result.