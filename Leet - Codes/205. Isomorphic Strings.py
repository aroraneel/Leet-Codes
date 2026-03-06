class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}

        for i, j in zip(s, t):
            if i in mapping:
                if mapping[i] != j:
                    return False
            else:
                mapping[i] = j

        if len(set(mapping.values())) != len(mapping.values()):
            return False

        newstr = ""
        for i in s:
            newstr += mapping[i]

        return newstr == t


if __name__ == "__main__":
    sol = Solution()

    s = "egg"
    t = "add"

    result = sol.isIsomorphic(s, t)

    print("String s:", s)
    print("String t:", t)
    print("Is Isomorphic?", result)

    # Summary:
    # This program checks whether two strings are isomorphic.
    # A mapping is created from characters in s to characters in t.
    # It ensures each character maps consistently and uniquely.
    # If the transformed string matches t, the strings are isomorphic.