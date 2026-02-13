from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix


if __name__ == "__main__":
    sol = Solution()

    strs = ["flower", "flow", "flight"]
    result = sol.longestCommonPrefix(strs)

    print("Strings:", strs)
    print("Longest Common Prefix:", result)

    # Summary:
    # This program finds the longest common prefix among a list of strings.
    # It starts with the first string as the prefix and checks each string.
    # If a string does not start with the prefix, the prefix is shortened
    # until it matches or becomes empty.
