class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1


if __name__ == "__main__":
    sol = Solution()

    haystack = "hello"
    needle = "ll"

    result = sol.strStr(haystack, needle)

    print("Haystack:", haystack)
    print("Needle:", needle)
    print("Index:", result)

    # Summary:
    # This program finds the first occurrence of the substring (needle)
    # inside the main string (haystack).
    # It checks each possible starting position using slicing.
    # If the substring is found, it returns the index, otherwise -1.
