from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        sorted_word = sorted(words, key=lambda x: -1 * len(x))

        encoding = ''
        indexes = []

        for word in sorted_word:
            position = encoding.find(word + '#')

            if position < 0:
                encoding += word + '#'

            indexes.append(position)

        return len(encoding)


sol = Solution()

words = ["feipyxx","e"]

print(sol.minimumLengthEncoding(words=words))
