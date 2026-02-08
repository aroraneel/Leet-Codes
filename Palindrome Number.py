class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    sol = Solution()

    x = 121
    result = sol.isPalindrome(x)

    print("Number:", x)
    print("Is Palindrome?", result)

    # Summary:
    # This program checks whether the given number is a palindrome.
    # It converts the number into a string and compares it with its reverse.

