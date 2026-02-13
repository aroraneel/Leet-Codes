class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]

        return total


if __name__ == "__main__":
    sol = Solution()

    s = "MCMXCIV"
    result = sol.romanToInt(s)

    print("Roman:", s)
    print("Integer:", result)

    # Summary:
    # This program converts a Roman numeral string into an integer.
    # It uses a dictionary to map each Roman symbol to its value.
    # If a smaller value comes before a larger one, it subtracts it.
    # Otherwise, it adds the value to the total.
