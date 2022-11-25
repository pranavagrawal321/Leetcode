class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_t = {}
        dict_s = {}
        for i in range(len(s)):
            if s[i] in dict_t and dict_t[s[i]] != t[i]:
                return False
            if t[i] in dict_s and dict_s[t[i]] != s[i]:
                return False
            dict_t[s[i]] = t[i]
            dict_s[t[i]] = s[i]
        return True
