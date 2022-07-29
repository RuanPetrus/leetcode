from typing import List, Tuple

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        stick = range(n + 1)
        better_cut = None
        n, _ = self.cut(stick, n)
        len(n)
        for i, n in enumerate(cuts):
            if 
        
        

    def cut(self, stick: List[int], n: int) -> Tuple[List[int], List[int]]:
        return stick[:n + 1], stick[n:] 

    def get_cost(self, stick: List[int]) -> int:
        return len(stick) - 1


########
# cuts = [5, 6, 1, 4, 2]
# stick = 0 1 2 3 4 5 6 7 8 9
#
# 4, sticks = 0 1 2 3 4 | 4 5 6 7 8 9, cost = 9
# 6, sticks = 0 1 2 3 4 | 4 5 6 | 6 5 8 9, cost = 5
#

