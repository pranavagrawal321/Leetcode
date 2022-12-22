class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {" ": " "}
        t = 97
        key = key.lower().replace(" ", "")
        for i in key:
            if i not in d:
                d[i] = chr(t)
                t += 1

        ans = ""
        for i in message:
            ans += d[i]

        return ans
