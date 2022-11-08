class Solution:
    def arrangeWords(self, s: str) -> str:
        s = s.split()
        return " ".join(sorted(s, key=lambda x:len(x))).capitalize()
