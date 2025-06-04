class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        newnum = num[::-1]
        return True if num == newnum else False

