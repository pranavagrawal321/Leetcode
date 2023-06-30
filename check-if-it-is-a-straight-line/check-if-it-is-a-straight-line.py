class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m = -float("inf") if coordinates[1][0] - coordinates[0][0] == 0 else (coordinates[1][1] - coordinates[0][1]) / (
        coordinates[1][0] - coordinates[0][0])

        for i in range(2, len(coordinates)):
            x1, y1, x2, y2 = coordinates[i - 1][0], coordinates[i - 1][1], coordinates[i][0], coordinates[i][1]
            slope = -float("inf") if x2 - x1 == 0 else(y2 - y1) / (x2 - x1)
            if slope != m:
                return False
        return True