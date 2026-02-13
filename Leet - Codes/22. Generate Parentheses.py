from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            if open_count == n and close_count == n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()

    n = 3
    result = sol.generateParenthesis(n)

    print("n =", n)
    print("Valid Parentheses Combinations:", result)

    # Summary:
    # This program generates all combinations of well-formed parentheses for n pairs.
    # It uses backtracking to build the string step by step.
    # An opening bracket can be added if open_count < n.
    # A closing bracket can be added only if close_count < open_count.
    # When both counts reach n, the combination is added to the result list.