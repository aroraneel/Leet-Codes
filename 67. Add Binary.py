class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).replace("0b", "")


if __name__ == "__main__":
    sol = Solution()

    a = "1010"
    b = "1011"
    result = sol.addBinary(a, b)

    print("Binary A:", a)
    print("Binary B:", b)
    print("Sum:", result)

    # Summary:
    # This program adds two binary strings and returns their sum as a binary string.
    # It converts both binary strings into integers, adds them,
    # then converts the result back into binary format.
    # The "0b" prefix is removed to return only the binary digits.
