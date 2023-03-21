class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0

        binary = bin(n)[2:][::-1]

        for i in range(len(binary)):
            if i % 2 == 0 and binary[i] == "1":
                even += 1
            elif i % 2 == 1 and binary[i] == "1":
                odd += 1

        return even, odd