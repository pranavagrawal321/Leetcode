class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return [True, False][(ord(coordinates[0]) + int(coordinates[1])) % 2 == 0]
