import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:

        heapq._heapify_max(target)
        s = sum(target)
        print(target)

        while target[0] != 1:
            sub = s - target[0]
            if sub < 1:
                return False
            n = max((target[0] - 1) // sub, 1)
            s -= n * sub
            target0 = target[0] - n * sub
            if target0 < 1:
                return False
            heapq._heapreplace_max(target, target0)
            print(target)

        return True


sol = Solution()
target = [9, 3, 5]
# target = [1,1,1,2]
# target = [8,5]
# target = [1,1000000000]

print(sol.isPossible(target))
