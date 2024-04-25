class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for i in range(len(s)):
            current_value = roman_values[s[i]]
            if i > 0 and current_value > prev_value:
                result += current_value - 2 * prev_value
            else:
                result += current_value
            prev_value = current_value

        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))      # Output: 3
    print(solution.romanToInt("LVIII"))    # Output: 58
    print(solution.romanToInt("MCMXCIV"))  # Output: 1994
    print(solution.romanToInt("IV"))       # Output: 4
    print(solution.romanToInt("IX"))       # Output: 9
    print(solution.romanToInt("MMMCMXCIX")) # Output: 3999
    print(solution.romanToInt(""))         # Output: 0
