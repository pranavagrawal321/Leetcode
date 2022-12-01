class Solution:
    def secondHighest(self, s: str) -> int:
        s = set(filter(lambda x: x.isdigit(), s))
        largest = -1
        second_largest = -1
        for i in s:
            if int(i) > largest:
                second_largest = largest
                largest = int(i)
            elif int(i) > second_largest:
                second_largest = int(i)
        return second_largest
