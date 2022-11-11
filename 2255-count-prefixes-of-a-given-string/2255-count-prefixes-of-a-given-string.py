class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        a = set()
        for i in range(len(s)):
            a.add(s[:i+1])

        c = 0
        for i in words:
            if i in a:
                c += 1
        return c
