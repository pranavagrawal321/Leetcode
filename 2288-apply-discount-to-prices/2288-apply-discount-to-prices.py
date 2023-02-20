class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        a = sentence.split()
        for i in range(len(a)):
            if a[i][0] == "$" and a[i][1:].isdigit():
                a[i] = "$" + '{0:.2f}'.format(int(a[i][1:])*(1 - discount/100))

        return " ".join(a)