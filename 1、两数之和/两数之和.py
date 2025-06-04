nums = [2,7,11,15]
target = 9


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1:]:
                return [i, nums[i+1:].index(res) + i + 1]