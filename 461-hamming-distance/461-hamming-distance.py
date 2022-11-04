class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b = bin(x)[2:], bin(y)[2:]
        if len(a) < len(b):
            a = (len(b) - len(a))*"0" + a
        elif len(b) < len(a):
            b = (len(a) - len(b))*"0" + b
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
        return c
