from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            initial = nums.index(target)
            total = 0
            for i in range(initial + 1, len(nums)):
                if nums[i] != nums[initial]:
                    break
                total += 1

            return [initial, initial + total]
        except:
            return [-1, -1]


sol = Solution()

print(sol.searchRange([5,7,7,8,8,10] ,8))
