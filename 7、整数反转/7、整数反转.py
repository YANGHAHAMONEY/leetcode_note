class Solution:
    def reverse(self, x: int) -> int:
        # 如果 x 是负数，递归反转其绝对值，并在最后返回负号
        if x < 0:
            return -self.reverse(-x)

        # 将整数反转
        reverse_x = int(str(x)[::-1])

        # 检查反转后的整数是否在32位有符号整数范围内
        if -2 ** 31 <= reverse_x < 2 ** 31:
            return reverse_x
        else:
            # 如果超出范围，返回0
            return 0