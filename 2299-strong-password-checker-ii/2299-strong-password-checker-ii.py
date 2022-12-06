class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        l, u, d, sp = 0, 0, 0, 0
        if len(s) < 8:
            return False


        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False

        for i in range(len(s)):
            if s[i].islower():
                l += 1
            elif s[i].isupper():
                u += 1
            elif s[i].isdigit():
                d += 1
            elif s[i] in "!@#$%^&*()-+":
                sp += 1
        # print(l, u, d, sp)
        return not (l == 0 or u == 0 or d == 0 or sp == 0)
