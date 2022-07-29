
class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_literals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                answer += roman_literals[i]

        return answer
