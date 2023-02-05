class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts[gifts.index(max(gifts))] = isqrt(max(gifts))

        return sum(gifts)