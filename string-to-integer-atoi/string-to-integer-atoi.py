class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        sign = ""
        num_start = False

        d = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

        for i in s.strip():
            if i in "+-" and num_start == False:
                sign += i
            elif i in d:
                ans = ans * 10 + d[i]
                num_start = True
            elif i not in d:
                break

        if len(sign) > 1:
            ans = 0
        else:
            if len(sign) == 0 or sign[0] == "+":
                print(ans)
            elif sign[0] == "-":
                ans = -ans

        if ans < -2 ** 31:
            ans = -2 ** 31
        elif ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1

        return ans