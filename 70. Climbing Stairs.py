class Solution:
    def climbStairs(self, n: int) -> int:
        def fun(n):
            if n < 2:
                return 1
            else:
                return fun(n - 1) + fun(n - 2)

        return fun(n)


if __name__ == "__main__":
    sol = Solution()

    n = 5
    result = sol.climbStairs(n)

    print("Number of stairs:", n)
    print("Ways to climb:", result)

    # Summary:
    # This program calculates the number of distinct ways to climb n stairs.
    # You can climb either 1 step or 2 steps at a time.
    # It uses recursion where fun(n) = fun(n-1) + fun(n-2).
    # The result follows the Fibonacci sequence pattern.
