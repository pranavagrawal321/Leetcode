class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set("qwertyuiop")
        b = set("asdfghjkl")
        c = set("zxcvbnm")


        def check(word, n):
            word = word.lower()
            if n == 0:
                for i in range(len(word)):
                    if word[i] not in a:
                        return False
                return True
            elif n == 1:
                for i in range(len(word)):
                    if word[i] not in b:
                        return False
                return True
            else:
                for i in range(len(word)):
                    if word[i] not in c:
                        return False
                return True


        ans = []
        for word in words:
            if word[0].lower() in a:
                n = 0
            elif word[0].lower() in b:
                n = 1
            else:
                n = 2
            if check(word, n):
                ans.append(word)
        return ans
