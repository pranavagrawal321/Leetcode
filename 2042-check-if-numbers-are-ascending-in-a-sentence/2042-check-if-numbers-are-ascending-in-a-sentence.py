class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = []
        s = s.split()
        for i in s:
            if i.isnumeric():
                l.append(int(i))

        for i in range(len(l)-1):
            if l[i] >= l[i+1]:
                return False
        return True
