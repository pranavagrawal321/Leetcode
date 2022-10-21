class SmallestInfiniteSet:

    def __init__(self):
        self.l = set(range(1, 1001))
        

    def popSmallest(self) -> int:
        m = min(self.l)
        self.l.remove(m)
        return m

    def addBack(self, num: int) -> None:
        self.l.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)