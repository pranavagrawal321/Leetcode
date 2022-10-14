class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a, b = s[:len(s)//2], s[len(s)//2:]
        ac = 0
        bc = 0

        for i in a:
            if i in "aeiou":
                ac += 1

        for i in b:
            if i in "aeiou":
                bc += 1

        return ac == bc