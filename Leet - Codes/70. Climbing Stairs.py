class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2

        for _ in range(3, n + 1):
            a, b = b, a + b

        return b


if __name__ == "__main__":
    sol = Solution()

    n = 44
    result = sol.climbStairs(n)

    print("Number of stairs:", n)
    print("Ways to climb:", result)

    # Summary:
    # This program finds the number of distinct ways to climb n stairs.
    # It uses an iterative dynamic programming approach (Fibonacci pattern),
    # avoiding slow recursion and passing all LeetCode test cases efficiently.