roman_table = {'I': 1, 
               'V': 5, 
               'X': 10, 
               'L': 50, 
               'C': 100, 
               'D': 500, 
               'M': 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        for i in range(0, len(s)):
            if i < (len(s) - 1) and roman_table[s[i]] < roman_table[s[i + 1]]:
                answer -= roman_table[s[i]]
                
            else:
                answer += roman_table[s[i]]
                
        return answer



solution = Solution()
print(solution.romanToInt("LVIII"))
