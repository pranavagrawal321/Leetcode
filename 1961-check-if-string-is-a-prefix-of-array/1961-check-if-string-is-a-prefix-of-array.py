class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        c = 0
        n = ""
        while len(n) < len(s) and c < len(words):
            n += words[c]
            c += 1
        return n == s
