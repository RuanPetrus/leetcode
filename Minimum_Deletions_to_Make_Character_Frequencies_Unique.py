from collections import Counter

class Solution:
        def minDeletions(self, s: str) -> int:
            freq = [number for number in dict(Counter(s)).values()]

            sorted_freq = sorted(freq, key=lambda x: -1 * x)

            counter = 0

            for i in range(len(sorted_freq) - 1):
                if sorted_freq[i] <= sorted_freq[i + 1]:
                    if sorted_freq[i] == 0:
                        sub = sorted_freq[i + 1]
                    else:
                        sub = abs(sorted_freq[i] - sorted_freq[i + 1]) + 1

                    sorted_freq[i + 1] -= sub
                    counter += sub

            return counter



sol = Solution()
s = "aaabbbcc"
s = "ceabaacb"
print(sol.minDeletions(s))

