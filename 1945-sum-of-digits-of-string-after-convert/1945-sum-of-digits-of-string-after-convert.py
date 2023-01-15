class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        for i in s:
            string += str(ord(i)-96)
        for i in range(k):
            string = str(sum(int(i) for i in string))
        return int(string)
