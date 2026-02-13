class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        if len(lst) == 0:
            return 0
        return len(lst[-1])


if __name__ == "__main__":
    sol = Solution()

    s = "Hello World"
    result = sol.lengthOfLastWord(s)

    print("String:", s)
    print("Length of Last Word:", result)

    # Summary:
    # This program finds the length of the last word in a given string.
    # It splits the string into words and checks the last element.
    # If the string has no words, it returns 0.
