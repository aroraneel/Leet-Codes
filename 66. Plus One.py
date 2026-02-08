from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join([str(i) for i in digits]))
        s += 1
        result = list(str(s))
        return [int(i) for i in result]


if __name__ == "__main__":
    sol = Solution()

    digits = [1, 2, 3]
    result = sol.plusOne(digits)

    print("Digits:", digits)
    print("After Plus One:", result)

    # Summary:
    # This program adds one to a number represented as an array of digits.
    # It converts the digits into an integer, increments it by one,
    # then converts the result back into a list of digits.
