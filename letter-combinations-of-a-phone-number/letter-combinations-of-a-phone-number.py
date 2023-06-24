class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        l = [d[i] for i in digits]
        ans = [*list(product(*l))]
        ans = ["".join(i) for i in ans]
        return ans