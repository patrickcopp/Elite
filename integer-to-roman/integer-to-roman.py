class Solution:
    def intToRoman(self, num: int) -> str:
        roman_array = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"],
        ]

        to_return = ""
        i = 0
        while i < len(roman_array):
            if num >= roman_array[i][0]:
                num -= roman_array[i][0]
                to_return += roman_array[i][1]
            else:
                i+=1
        return to_return