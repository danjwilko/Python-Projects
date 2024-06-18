class Solution:
    def romanToInt(self, s: str) -> int:

        num = 0
        last = 'I'
        roman_numeral_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        for numeral in s[::-1]:
            if roman_numeral_values[numeral] < roman_numeral_values[last]:
                num -= int(roman_numeral_values[numeral])
            else:
                num += int(roman_numeral_values[numeral])
                last = numeral
        return num