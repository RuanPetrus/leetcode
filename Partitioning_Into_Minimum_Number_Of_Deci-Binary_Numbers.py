class Solution:
    def minPartitions(self, n: str) -> int:
        interger_array = [int(x) for x in n]
        return max(interger_array)
