class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[0] if target < letters[0] or target >= letters[-1] else letters[bisect.bisect_right(letters, target)]