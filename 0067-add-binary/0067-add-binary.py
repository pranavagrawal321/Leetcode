class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 and j >= 0:
            if a[i] == b[j] == "1":
                ans += str(carry)
                carry = 1
            elif a[i] == b[j] == "0":
                ans += str(carry)
                carry = 0
            else:
                if carry == 1:
                    ans += "0"
                else:
                    ans += "1"
            i -= 1
            j -= 1

        while i >= 0:
            if carry == 1:
                if a[i] == "1":
                    ans += "0"
                else:
                    ans += "1"
                    carry = 0
            else:
                ans += a[i]
            i -= 1

        while j >= 0:
            if carry == 1:
                if b[j] == "1":
                    ans += "0"
                else:
                    ans += "1"
                    carry = 0
            else:
                ans += b[j]
            j -= 1

        if carry == 1:
            ans += "1"

        return ans[::-1]