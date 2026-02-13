class Solution:
    def intToRoman(self, num: int) -> str:
        val_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        roman = ""

        for value, symbol in val_map:
            while num >= value:
                roman += symbol
                num -= value

        return roman


if __name__ == "__main__":
    sol = Solution()

    num = 1994
    result = sol.intToRoman(num)

    print("Number:", num)
    print("Roman Numeral:", result)

    # Summary:
    # This program converts an integer into a Roman numeral.
    # It uses a list of value-symbol pairs and repeatedly subtracts
    # the largest possible value while adding its Roman symbol.
    # The final built string is returned as the Roman numeral.