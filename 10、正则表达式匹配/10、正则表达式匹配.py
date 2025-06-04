class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from re import search
        return bool(search(r"^" + p + r"$", s))

