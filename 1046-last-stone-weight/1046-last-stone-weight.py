class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.append(0)
        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if x == y:
                pass
            else:
                stones.append(abs(x-y))

        return stones[0]