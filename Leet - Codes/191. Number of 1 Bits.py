class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if (n & 1) == 1:
                count += 1
            n = n >> 1
        return count


if __name__ == "__main__":
    sol = Solution()

    n = 11
    result = sol.hammingWeight(n)

    print("Number:", n)
    print("Binary:", bin(n))
    print("Hamming Weight:", result)

    # Summary:
    # This program counts the number of 1 bits in the binary representation of a number.
    # It checks the last bit using (n & 1).
    # Then it right shifts the number until it becomes zero.
    # The count of 1 bits is returned.