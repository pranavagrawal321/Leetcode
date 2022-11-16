class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
        stack2 = []
        for i in t:
            if i != "#":
                stack2.append(i)
            else:
                if stack2:
                    stack2.pop()
        return stack == stack2
