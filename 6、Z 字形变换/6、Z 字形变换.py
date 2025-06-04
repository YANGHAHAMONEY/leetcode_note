class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:return s
        array = [s for i in range(numRows)]
        ans = [list() for i in range(numRows)]
        i, direction = 0, 1
        for j in range(len(s)):
            ans[i].append(array[i][j])
            i += direction
            if i == 0 or i == numRows - 1:
                direction *= -1
        result = list()
        for i in ans:
            result.extend(i)
        #   最后转换成字符串返回
        return ''.join(result)