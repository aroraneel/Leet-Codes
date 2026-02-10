class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)


if __name__ == "__main__":
    sol = Solution()

    x = 8
    result = sol.mySqrt(x)

    print("Number:", x)
    print("Square Root (Integer Part):", result)

    # Summary:
    # This program finds the integer square root of a number.
    # It computes the square root using exponentiation (x**0.5)
    # and converts it to an integer, which removes the decimal part.
