class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set("aeiouAEIOU")
        start = 0
        end = len(s)-1

        while start <= end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] not in vowels and s[end] not in vowels:
                start += 1
                end -= 1
            elif s[start] not in vowels:
                start += 1
            else:
                end -= 1

        return "".join(s)