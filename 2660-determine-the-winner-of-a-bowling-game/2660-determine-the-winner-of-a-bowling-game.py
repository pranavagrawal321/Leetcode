class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = sum(player1)
        score2 = sum(player2)
        if len(player1) > 1:
            for i in range(1, len(player1)):
                if player1[i - 1] == 10 or (i >=2 and player1[i - 2] == 10):
                    score1 += player1[i]

            for i in range(1, len(player2)):
                if player2[i - 1] == 10 or (i >= 2 and player2[i - 2] == 10):
                    score2 += player2[i]

        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0