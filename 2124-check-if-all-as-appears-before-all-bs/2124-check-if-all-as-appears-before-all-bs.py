class Solution:
    def checkString(self, s: str) -> bool:
        try:
            return s.rindex("a") < s.index("b")
        except ValueError:
            return True
