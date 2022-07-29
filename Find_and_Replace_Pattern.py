from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_key_from_value(d, val):
            return [k for k, v in d.items() if v == val][0]

        pattern_matched = []
        for word in words:
            table = {}
            matched = True
            for i, letter in enumerate(word):
                if (letter in table.keys() and table[letter] != pattern[i]) or (
                    pattern[i] in table.values()
                    and letter != get_key_from_value(table, pattern[i])
                ):
                    matched = False
                    break

                else:
                    table[letter] = pattern[i]

            if matched:
                pattern_matched.append(word)

        return pattern_matched


sol = Solution()
print(sol.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
