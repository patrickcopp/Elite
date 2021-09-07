class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        current_char = 0
        total = 0
        while current_char < len(s):
            if current_char + 1 < len(s) and s[current_char:current_char + 2] in roman_dict:
                total += roman_dict[s[current_char:current_char + 2]]
                current_char += 2
            else:
                total += roman_dict[s[current_char]]
                current_char += 1
        return total
            