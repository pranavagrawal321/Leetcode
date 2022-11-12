class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = ""
        for i in words:
            if len(n) < len(s):
                n += i
            else:
                break
        return n == s
