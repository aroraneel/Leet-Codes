class Solution:
    def reverseBits(self, n: int) -> int:
        result, power = 0, 31

        while n > 0:
            result += (n & 1) << power
            n = n >> 1
            power -= 1

        return result


if __name__ == "__main__":
    sol = Solution()

    n = 43261596
    result = sol.reverseBits(n)

    print("Original Number:", n)
    print("Binary:", bin(n))
    print("Reversed Bits Result:", result)
    print("Reversed Binary:", bin(result))

    # Summary:
    # This program reverses the bits of a 32-bit unsigned integer.
    # It extracts each bit using (n & 1) and places it in the correct reversed position.
    # The power variable tracks the position from 31 down to 0.
    # The final result is the integer formed after reversing all bits.