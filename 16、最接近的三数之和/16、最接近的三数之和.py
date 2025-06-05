class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 数组的长度，长度为三时，直接返回就好
        n = len(nums)
        if n == 3: return nums[0] + nums[1] + nums[2]
        # 升序排序
        nums.sort()
        x = nums[0] + nums[1] + nums[2]
        # 如果最小的三个值，都大于target，则直接返回即可，因为后续的只会更大
        if x >= target: return x

        # 记录最小的时候的差，以及三个数之和
        min = abs(x - target)
        min_ = x
        for i in range(0, n - 2):
            left = i + 1  # 左端
            right = n - 1  # 右端
            while left < right:
                x = nums[i] + nums[left] + nums[right]
                if abs(x - target) < min:  # 更新最小的差，以及三个数之和
                    min = abs(x - target)
                    min_ = x
                if (x - target) > 0:
                    right -= 1  # 大于时右端左移
                elif (x - target) < 0:
                    left += 1  # 小于时左端右移
                else:
                    return x  # 相等时直接返回
        return min_


