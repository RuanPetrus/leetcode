from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in nums and i != nums.index(sub):
                return [i, nums.index(target - nums[i])]
