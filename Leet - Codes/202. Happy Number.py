class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()

        while n != 1:
            sqrSum = 0
            for i in str(n):
                sqrSum += int(i) ** 2

            n = sqrSum

            if n in mem:
                return False
            else:
                mem.add(n)

        return True


if __name__ == "__main__":
    sol = Solution()

    n = 19
    result = sol.isHappy(n)

    print("Number:", n)
    print("Is Happy Number?", result)

    # Summary:
    # This program checks whether a number is a happy number.
    # It repeatedly replaces the number with the sum of squares of its digits.
    # A set is used to detect cycles in the sequence.
    # If the number becomes 1, it is a happy number; if a cycle appears, it is not.