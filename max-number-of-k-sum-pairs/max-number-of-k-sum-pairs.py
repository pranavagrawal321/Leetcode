class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = set()
        c = Counter(nums)

        for i in c:
            if i not in seen and k-i in c:
                if i == k-i:
                    ans += c[i]//2
                else:
                    ans += min(c[i], c[k-i])
                    seen.add(i)
                    seen.add(k-i)
                
        return ans