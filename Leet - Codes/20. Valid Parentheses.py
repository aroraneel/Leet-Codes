class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack[-1] != pair[char]:
                    return False
                stack.pop()

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()

    s = "()[]{}"
    result = sol.isValid(s)

    print("String:", s)
    print("Is Valid?", result)

    # Summary:
    # This program checks whether the given string of brackets is valid.
    # It uses a stack to store opening brackets as they appear.
    # When a closing bracket is found, it checks if it matches the last opening one.
    # The string is valid only if all brackets are properly matched and the stack is empty.
