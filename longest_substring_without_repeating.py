
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s) - 1):
            first = s[i]
            seem = [first]

            next = s[i + 1]
            count = 1

            while next not in seem and i + count < len(s) - 1:
                count += 1
                seem.append(next)

                next = s[i + count]
               
            if count > longest:
                longest = count

        return longest


sol = Solution()

print(sol.lengthOfLongestSubstring('bbbbb'))
