words = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
dct = {f"{i + 2}": word for i, word in enumerate(words)}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(pre, j):
            if j == n:
                if pre:
                    ans.append(pre)
                return
            for w in dct[digits[j]]:
                dfs(pre + w, j + 1)
            return

        n = len(digits)
        ans = []
        dfs("", 0)
        return ans
