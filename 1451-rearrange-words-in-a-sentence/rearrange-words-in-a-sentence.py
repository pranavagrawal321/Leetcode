class Solution:
    def arrangeWords(self, s: str) -> str:
        d = {}
        s = s.split()
        for i in s:
            if len(i) in d:
                d[len(i)].append(i)
            else:
                d[len(i)] = [i]

        output = ""
        for i in sorted(d):
            output += " ".join(d[i]) + " "

        return output[:-1].capitalize()
