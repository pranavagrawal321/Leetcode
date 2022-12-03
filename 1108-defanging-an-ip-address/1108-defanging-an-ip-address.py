class Solution:
    def defangIPaddr(self, s: str) -> str:
        s = s.replace(".", "[.]")
        return s
