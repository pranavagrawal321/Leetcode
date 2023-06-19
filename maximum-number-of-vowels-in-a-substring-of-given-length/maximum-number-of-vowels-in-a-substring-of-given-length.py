class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        final = 0
        for i in range(k):
            if s[i] in {"a", "e", "i", "o", "u"}:
                final += 1

        pointer = 0
        temp = final
        for i in range(k, len(s)):
            if s[pointer] in {"a", "e", "i", "o", "u"}:
                temp -= 1
            if s[i] in {"a", "e", "i", "o", "u"}:
                temp += 1
            final = max(final, temp)
            pointer += 1

        return final