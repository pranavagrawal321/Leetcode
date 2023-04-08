class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1 = int(event1[0][:2])*60 + int(event1[0][3:])
        start2 = int(event2[0][:2])*60 + int(event2[0][3:])
        end1 = int(event1[1][:2])*60 + int(event1[1][3:])
        end2 = int(event2[1][:2])*60 + int(event2[1][3:])

    return start1 <= start2 <= end1 or start1 <= end2 <= end1 or start2 <= start1 <= end2 or start2 <= end1 <= end2