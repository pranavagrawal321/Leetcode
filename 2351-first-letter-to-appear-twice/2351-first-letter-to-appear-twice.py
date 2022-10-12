class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashset = set()
        for i in s:
            if i not in hashset:
                hashset.add(i)
            else:
                return i