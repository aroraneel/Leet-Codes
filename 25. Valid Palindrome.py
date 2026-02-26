class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for i in s:
            if i.isalnum():
                r += i
        r = r.lower()
        if r == r[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()

    s = "A man, a plan, a canal: Panama"
    result = sol.isPalindrome(s)

    print("Original String:", s)
    print("Is Palindrome?", result)

    # Summary:
    # This program checks if a string is a valid palindrome.
    # It removes all non-alphanumeric characters.
    # Then it converts the string to lowercase.
    # Finally, it compares the cleaned string with its reverse.